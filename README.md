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

## Content

This repository contains two main files describing concepts and code about diverse topics in descriptive and inferential statistic. In this way, the index is as follows:

### [**01_DescriptiveStatistics.ipynb**](https://github.com/Luis-Alat/Study_Notebooks/blob/main/01_DescriptiveStatistics.ipynb)

1. Standard deviation and Chebyshev teorem

2. Z-score standarization and probability distribution function

3. Quartiles, IQR or Interquartile Range and BoxPlot

4. Covariance and Coefficient of variations

5. Asymmetry and Kurtosis

6. Standard error and Confidence interval


### [**02_InferentialStatistic.ipynb**](https://github.com/Luis-Alat/Study_Notebooks/blob/main/02_InferentialStatistic.ipynb)

1. Confidence Intervals (CI) and Bootstrapping

2. P-value

3. Parametric tests

    * T-test
        
        * F-test
    
    * Z-test

    * T-test vs Z-test

    * Anova
        
        * One-way Anova in R

        * Two-way Anova

        * Paired Anova

        * Sum of squares Type I,II and III

    * Manova

    * Ancova

    * Mancova

4. Non-parametric tests

    * Sign-test

    * Wilcoxon signed-rank test

    * Mann-Whitney test

    * Kruskal-Wallis test

    * Friedman test

    * Fisher's test

    * Chi-squared test

    * G-test

## Notes

* For a better display of the notebook (for some plotly plots), I recommed the use of **nbviewer** at https://nbviewer.org/
