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

# How do I use the toolbox with my data?
1. Put your data that can be read into a DataFrame using Pandas. We use Pandas' "read_csv" function in our examples, which requires the data to be in CSV format - see any of the top-level scripts for examples. 
2. Use Replicate_Figure1.py as a template. Make a copy (e.g. My_Strategy_Analysis.py). Edit that copy to load your data (in the format of Step 1) and select the strategies you want to apply (in the list "strategues = ['go_left',...,]); then run it and see the results
3. Write your own strategy models: see the strategymodels.py module for examples and a template. All strategy model functions have the same input (rows of the DataFrame up to the current trial) and output (the trial type as a string). Then simply add the name of the new function to your list of strategies in your script. And run it!
