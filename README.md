# Basic molecular descriptors from Datamol

Basic molecular descriptors calculated with the Datamol package, including molecular weight, lipophilicity (cLogP), hydrogen bond donnors, hydrogen bond acceptors, etc. These descriptors are generally useful to annotate small molecule libraries. They are not recommended for QSAR modeling since they are probably too simple for most scenarios.

## Identifiers

* EOS model ID: `eos4djh`
* Slug: `datamol-basic-descriptors`

## Characteristics

* Input: `Compound`
* Input Shape: `Single`
* Task: `Representation`
* Output: `Descriptor`
* Output Type: `Float`
* Output Shape: `List`
* Interpretation: Basic molecular descriptors. Some descriptors are floats and some are counts.

## References

* [Publication](https://github.com/datamol-io/datamol)
* [Source Code](https://docs.datamol.io/0.7.4/api/datamol.descriptors.html)
* Ersilia contributor: [miquelduranfrigola](https://github.com/miquelduranfrigola)

## Ersilia model URLs
* [GitHub](https://github.com/ersilia-os/eos4djh)
* [AWS S3](https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos4djh.zip)
* [DockerHub](https://hub.docker.com/r/ersiliaos/eos4djh) (AMD64, ARM64)

## Citation

If you use this model, please cite the [original authors](https://github.com/datamol-io/datamol) of the model and the [Ersilia Model Hub](https://github.com/ersilia-os/ersilia/blob/master/CITATION.cff).

## License

This package is licensed under a GPL-3.0 license. The model contained within this package is licensed under a Apache-2.0 license.

Notice: Ersilia grants access to these models 'as is' provided by the original authors, please refer to the original code repository and/or publication if you use the model in your research.

## About Us

The [Ersilia Open Source Initiative](https://ersilia.io) is a Non Profit Organization ([1192266](https://register-of-charities.charitycommission.gov.uk/charity-search/-/charity-details/5170657/full-print)) with the mission is to equip labs, universities and clinics in LMIC with AI/ML tools for infectious disease research.

[Help us](https://www.ersilia.io/donate) achieve our mission!