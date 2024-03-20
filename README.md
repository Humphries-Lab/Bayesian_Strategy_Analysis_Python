# Bayesian_Strategy_Analyisis_Python

Python toolbox for Bayesian analysis of behavioural strategies on choice tasks

Read the paper at eLife: https://doi.org/10.7554/eLife.86491

Tested with: Python 3.9 onwards

(This is a Python port of https://github.com/Humphries-Lab/Bayesian_Strategy_Analysis_MATLAB)

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
1. Put your data into a format that can be read into a DataFrame using Pandas. We use Pandas' "read_csv" function in our examples, which requires the data to be in CSV format - see any of the top-level scripts for examples. 
2. Use Replicate_Figure1.py as a template. Make a copy (e.g. My_Strategy_Analysis.py). Edit that copy to load your data (in the format of Step 1) and select the strategies you want to apply (in the list "strategies = ['go_left',...,]); then run it and see the results
3. Write your own strategy models: see the strategymodels.py module for examples and a template. All strategy model functions have the same input (rows of the DataFrame up to the current trial) and output (the trial type as a string). Then simply add the name of the new function to your list of strategies in your script. And run it!

# Things to be aware of
- Names and values of data variables: the supplied strategy models assume that the loaded dataset uses the following names and values for each variable: Choice ("left","right'), Reward ("yes","no"), CuePosition ("left","right"). 

- Omissions: the supplied strategy functions assume the subject made a choice on each trial. If your data contain trials with omissions (e.g. the subject did not engage on that trial) then either (a) remove those trials from the dataset before using the strategy analysis on them, or (b) edit the code to handle how you coded the omissions in your data. For example, if you coded an omission as Choice = NaN, then assign any trial with Choice = NaN as a "null" trial-type for *every* strategy; the best place to do that would be in the top-level script -- an if/else that checked first whether the trial was an omission, and then only evaluated the trial-type for each strategy if it was not an omission.

# Problems?
- Raise an "Issue" here on the GitHub repository. In the "Issue" give the problem/bug you came across (and where) or the question you have about how to use the toolbox
