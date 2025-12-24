# imports
import os
import sys
import numpy as np
import datamol as dm
from ersilia_pack_utils.core import read_smiles, write_out

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

# read input
_, smiles_list = read_smiles(input_file)

# run model
outputs = datamol_featurizer(smiles_list)

#check input and output have the same lenght
input_len = len(smiles_list)
output_len = len(outputs)
assert input_len == output_len

write_out(outputs, columns, output_file, np.float32)
