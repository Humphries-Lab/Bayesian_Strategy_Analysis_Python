#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 24 11:48:26 2022

@author: Lowri Powell & Mark Humphries
"""
import matplotlib.pyplot as plt
import numpy as np


def plotSessionStructure(TestData):
    no_Trials = np.size(TestData.TrialIndex)
    
    sessionLines = TestData[TestData['NewSessionTrials'] == 1].index  # indices list  when new session was started
    plt.vlines(sessionLines, 0, 1, colors='lightgray', linestyles='--', linewidth=0.75,
               label="New Sessions")  # vertical lines indicate the new session trials
    ruleLines = np.array(TestData[TestData['RuleChangeTrials'] == 1].index)  # indices list  when new session was started
    ruleLines = np.insert(ruleLines, 0, 0)  # sets array for x values of rule change

    for x in ruleLines:  # to get shade change for rule change and labels
        minx = x / no_Trials
        plt.axhspan(1, 1.25, xmin=minx, alpha=0.3, edgecolor='k')  # change transparency for separation
        plt.axvline(x, 0.8, 1)  # dividing lines

    #  creating labels
    plt.text(1, 1.125, "Right Arm", label='Go to the Right')
    plt.text(120, 1.125, "Lit Arm", label='Go to the Lit Arm')
    plt.text(225, 1.125, "Left Arm", label='Go to the Left')
    plt.text(330, 1.125, "Unlit Arm", label='Go to the Dark Arm')
    plt.text(150, 1.3, "Rule for Reward")
    plt.legend()  # add legend