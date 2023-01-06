# Study_Notebooks
Notebooks developed while self-studying topics of interest to me. It is not intended to be a guide of any kind.

## Getting started

Two conda environments are available to run the notebooks locally (see below) if you want. In this regard, I highly recommend mamba to handle the importing of the enviroment because of Conda may face problems about lack of memory. Anyway, the sintax is basically the same between both of them

### Importing across platforms 

Enviroment created using the option --from-history

Using conda

	conda env create --file environment_FH.yml
		
Using mamba

	mamba env create --file environment_FH.yml

### Importing for ubuntu 20.04

Enviroment created using the option --no-builds

Using conda

    conda env create --file environment_NB.yml

Using mamba

    mamba env create --file environment_NB.yml
