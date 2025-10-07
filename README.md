# Basic molecular descriptors from Datamol

Basic molecular descriptors calculated with the Datamol package, including molecular weight, lipophilicity (cLogP), hydrogen bond donnors, hydrogen bond acceptors, etc. These descriptors are generally useful to annotate small molecule libraries. They are not recommended for QSAR modeling since they are probably too simple for most scenarios.

This model was incorporated on 2024-11-09.


## Information
### Identifiers
- **Ersilia Identifier:** `eos4djh`
- **Slug:** `datamol-basic-descriptors`

### Domain
- **Task:** `Representation`
- **Subtask:** `Featurization`
- **Biomedical Area:** `Any`
- **Target Organism:** `Any`
- **Tags:** `Descriptor`

### Input
- **Input:** `Compound`
- **Input Dimension:** `1`

### Output
- **Output Dimension:** `22`
- **Output Consistency:** `Fixed`
- **Interpretation:** Basic molecular descriptors. Some descriptors are floats and some are counts.

Below are the **Output Columns** of the model:
| Name | Type | Direction | Description |
|------|------|-----------|-------------|
| mw | float | high | Molecular weight of the compound |
| fsp3 | float | high | Fraction of sp3 hybridized carbons |
| n_lipinski_hba | integer | high | Number of Lipinski hydrogen bond acceptors |
| n_lipinski_hbd | integer | high | Number of Lipinski hydrogen bond donors |
| n_rings | integer | high | Number of rings in the compound |
| n_hetero_atoms | integer | high | Number of heteroatoms in the compound |
| n_heavy_atoms | integer | high | Number of heavy atoms non-hydrogen in the compound |
| n_rotatable_bonds | integer | high | Number of rotatable bonds in the compound |
| n_radical_electrons | integer | high | Number of radical electrons in the compound |
| tpsa | float | high | Topological polar surface area of the compound |

_10 of 22 columns are shown_
### Source and Deployment
- **Source:** `Local`
- **Source Type:** `External`
- **DockerHub**: [https://hub.docker.com/r/ersiliaos/eos4djh](https://hub.docker.com/r/ersiliaos/eos4djh)
- **Docker Architecture:** `AMD64`, `ARM64`
- **S3 Storage**: [https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos4djh.zip](https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos4djh.zip)

### Resource Consumption
- **Model Size (Mb):** `1`
- **Environment Size (Mb):** `804`
- **Image Size (Mb):** `723.23`

**Computational Performance (seconds):**
- 10 inputs: `30.79`
- 100 inputs: `21.09`
- 10000 inputs: `318.44`

### References
- **Source Code**: [https://docs.datamol.io/0.7.4/api/datamol.descriptors.html](https://docs.datamol.io/0.7.4/api/datamol.descriptors.html)
- **Publication**: [https://github.com/datamol-io/datamol](https://github.com/datamol-io/datamol)
- **Publication Type:** `Other`
- **Publication Year:** `2024`
- **Ersilia Contributor:** [miquelduranfrigola](https://github.com/miquelduranfrigola)

### License
This package is licensed under a [GPL-3.0](https://github.com/ersilia-os/ersilia/blob/master/LICENSE) license. The model contained within this package is licensed under a [Apache-2.0](LICENSE) license.

**Notice**: Ersilia grants access to models _as is_, directly from the original authors, please refer to the original code repository and/or publication if you use the model in your research.


## Use
To use this model locally, you need to have the [Ersilia CLI](https://github.com/ersilia-os/ersilia) installed.
The model can be **fetched** using the following command:
```bash
# fetch model from the Ersilia Model Hub
ersilia fetch eos4djh
```
Then, you can **serve**, **run** and **close** the model as follows:
```bash
# serve the model
ersilia serve eos4djh
# generate an example file
ersilia example -n 3 -f my_input.csv
# run the model
ersilia run -i my_input.csv -o my_output.csv
# close the model
ersilia close
```

## About Ersilia
The [Ersilia Open Source Initiative](https://ersilia.io) is a tech non-profit organization fueling sustainable research in the Global South.
Please [cite](https://github.com/ersilia-os/ersilia/blob/master/CITATION.cff) the Ersilia Model Hub if you've found this model to be useful. Always [let us know](https://github.com/ersilia-os/ersilia/issues) if you experience any issues while trying to run it.
If you want to contribute to our mission, consider [donating](https://www.ersilia.io/donate) to Ersilia!
