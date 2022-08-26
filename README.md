# Bayesian_Strategy_Analyisis_Python

Python toolbox for Bayesian analysis of behavioural strategies on choice tasks

(This is a Python port of https://github.com/Humphries-Lab/Bayesian_Strategy_Analysis_MATLAB)

Tested with: Python 3.9 onwards

[reference to pre-print to go here]

## Top-level scripts
Two scripts demonstrate the main use of the Toolbox:
1. Demonstrate_Bayesian_strategy_analysis.m: shows how to run the algorithm for a single strategy model  
2. Replicate_Figure1: replicates panels c, d, and e of Figure 1 in the paper, to demonstrate the full workflow: choosing strategies, computing p(strategy) for each, interpolating probabilities for Null trials, and then plotting the appropriate time-series of probabilities

## Modules
- strategymodels.py contains functions that implement the strategy models

## Data
- data.csv: data from Rat 2 of the Peyrache et al 2009 (Nat Neurosci) study of Y-maze performance (see pre-print for details)

## Folders
- Functions/: the set of functions that implement the Bayesian algorithm and summarise the Beta distribution (MAP estimate, precision etc)

