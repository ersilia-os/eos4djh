# imports
import os
import csv
import sys
import json
import struct
import numpy as np
import datamol as dm
from tqdm import tqdm

# parse arguments
input_file = sys.argv[1]
output_file = sys.argv[2]

# current file directory
root = os.path.dirname(os.path.abspath(__file__))

columns = [
    "mw",
    "fsp3",
    "n_lipinski_hba",
    "n_lipinski_hbd",
    "n_rings",
    "n_hetero_atoms",
    "n_heavy_atoms",
    "n_rotatable_bonds",
    "n_radical_electrons",
    "tpsa",
    "qed",
    "clogp",
    "sas",
    "n_aliphatic_carbocycles",
    "n_aliphatic_heterocyles",
    "n_aliphatic_rings",
    "n_aromatic_carbocycles",
    "n_aromatic_heterocyles",
    "n_aromatic_rings",
    "n_saturated_carbocycles",
    "n_saturated_heterocyles",
    "n_saturated_rings"
]

# calculate descriptors for the molecules 
def datamol_featurizer(smiles_list):
    R = []
    for smiles in smiles_list:
        mol = dm.to_mol(smiles)
        descriptors = dm.descriptors.compute_many_descriptors(mol)
        r = [descriptors[k] for k in columns]
        R.append(r)
    return R


# functions to read and write .csv and .bin files
def read_smiles_csv(in_file): # read SMILES from .csv file, assuming one column with header
  with open(in_file, "r") as f:
    reader = csv.reader(f)
    cols = next(reader)
    data = [r[0] for r in reader]
    return cols, data

def read_smiles_bin(in_file):
  with open(in_file, "rb") as f:
    data = f.read()

  mv = memoryview(data)
  nl = mv.tobytes().find(b"\n")
  meta = json.loads(mv[:nl].tobytes().decode("utf-8"))
  cols = meta.get("columns", [])
  count = meta.get("count", 0)
  smiles_list = [None] * count
  offset = nl + 1
  for i in range(count):
    (length,) = struct.unpack_from(">I", mv, offset)
    offset += 4
    smiles_list[i] = mv[offset : offset + length].tobytes().decode("utf-8")
    offset += length
  return cols, smiles_list

def read_smiles(in_file):
  if in_file.endswith(".bin"):
    return read_smiles_bin(in_file)
  return read_smiles_csv(in_file)

def write_out_csv(results, header, file):
  with open(file, "w") as f:
    writer = csv.writer(f)
    writer.writerow(header)
    for r in results:
      writer.writerow(r)

def write_out_bin(results, header, file):
  arr = np.asarray(results, dtype=np.float32)
  meta = {"columns": header, "shape": arr.shape, "dtype": "float32"}
  meta_bytes = (json.dumps(meta) + "\n").encode("utf-8")
  with open(file, "wb") as f:
    f.write(meta_bytes)
    f.truncate(len(meta_bytes) + arr.nbytes)
  m = np.memmap(
    file, dtype=arr.dtype, mode="r+", offset=len(meta_bytes), shape=arr.shape
  )
  m[:] = arr
  m.flush()

def write_out(results, header, file):
  if file.endswith(".bin"):
    write_out_bin(results, header, file)
  elif file.endswith(".csv"):
    write_out_csv(results, header, file)
  else:
    raise ValueError(f"Unsupported extension for {file!r}")

# read input
_, smiles_list = read_smiles(input_file)

# run model
outputs = datamol_featurizer(smiles_list)

#check input and output have the same lenght
input_len = len(smiles_list)
output_len = len(outputs)
assert input_len == output_len

write_out(outputs, columns, output_file)
