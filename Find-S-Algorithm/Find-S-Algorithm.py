# -*- coding: utf-8 -*-
"""
Created on Fri Sep 10 21:16:25 2021

@author: Nishant Kumar
"""
# load important libraries
import numpy as np
import pandas as pd

# load dataset
dataset = pd.read_csv('D:/MTech(NITK)/Machine Learning/ML Lab/Find-S-Algorithm/find-S.csv')

print("Original Data:\n",dataset, "\n\n")

# Making an arrray of dataset
arr = np.array(dataset)[:,:-1]
print("Data in array:\n", arr, "\n\n")

# find the target values so the target is -ve and +ve values
target_values = np.array(dataset)[:,-1]
print("Target values : ", target_values, "\n")

# Find-S-Algorithm function
def findMostSpecificHypothesis(data, target):
    for i, val in enumerate(target):
        if val == "yes":
            specific_hypothesis = data[i].copy()
            break
    
    for j, val in enumerate(data):
        if target[j] == "yes":
            for x in range(len(specific_hypothesis)):
                if val[x] != specific_hypothesis[x]:
                    specific_hypothesis[x] = '?'
                else:
                    pass
    return specific_hypothesis
            
            
# final hypthesis result
print("The final hypothesis result : ", findMostSpecificHypothesis(arr, target_values))          
            
            
            
            
            
            