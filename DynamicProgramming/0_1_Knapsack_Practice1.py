# -*- coding: utf-8 -*-
"""
Created on Sat Jan  8 15:10:40 2022

@author: Luv Verma
"""

# =============================================================================
# Input:
#  
# value = [ 20, 5, 10, 40, 15, 25 ]
# weight = [ 1, 2, 3, 8, 7, 4 ]
# int W = 10
# Constraint is weight. Weight should either be less or equal to 
# the constraint. 
# =============================================================================

def knapsackWrongCode(TV,WC,i=4,solutions = []):
    value = [ 20, 30,15,25,10]
    weight = [ 6,13,5,10,3]
    
    #print(solutions)
    if WC < 0:
        return
    if WC == 0:
        solutions.append(TV)
        #return solutions
    while i >0:
        #print("i,TV+value[i], WC",i,TV+value[i],WC)
        knapsackWrongCode(TV+value[i], WC-weight[i], i,solutions)
        i = i-1
        
    return solutions
(knapsackWrongCode(TV=0,WC=20))
    
def knapsackRecursion(value, weight,TV,WC,i):
    
    if i == len(value):
        return 0
    if weight[i]>WC:
        knapsackRecursion(value, weight,TV,WC,i+1)
        #return TV
    #print(knapsackRecursion(value, weight,TV,WC-weight[i],i+1))
    else:
        TV = max(value[i]+knapsackRecursion(value, weight,TV,WC-weight[i],i+1), knapsackRecursion(value, weight,TV,WC,i+1))
    return TV
    
    

value = [ 20, 30,15,25,10]
weight = [ 6,13,5,10,3]
print(knapsackRecursion(value, weight,TV=0,WC=20,i=0))
print("===================================>")
value = [60, 100, 120]
weight = [10, 20, 30]
WC = 50
print(knapsackRecursion(value, weight,TV=0,WC=WC,i=0))

#==========================================>
print("===================================>")

def knapsackMemoization(value, weight,TV,WC,i, lookup= {}):
    if (WC,i) in lookup:
        return lookup[(WC,i)]
    if i == len(value):
        return 0
    if weight[i]>WC:
        
        lookup[(WC,i)]=knapsackMemoization(value, weight,TV,WC,i+1)
        
        #return TV
    #print(knapsackRecursion(value, weight,TV,WC-weight[i],i+1))
    else:
        
        TV = max(value[i]+knapsackMemoization(value, weight,TV,WC-weight[i],i+1), knapsackMemoization(value, weight,TV,WC,i+1))
        lookup[(WC,i)] = TV
        print(WC)
    return lookup[(WC,i)]  

print("===================================>")
value = [60, 100, 120]
weight = [10, 20, 30]
WC = 50
print(knapsackMemoization(value, weight,TV=0,WC=WC,i=0))
print("=============>")
value = [ 20, 30,15,25,10]
weight = [ 6,13,5,10,3]
print(knapsackMemoization(value, weight,TV=0,WC=20,i=0))
print("=============>")
print("==========================================>")

# =============================================================================
# print("Algorithm")
# # i ==> i for the movement from 1 row to next
# # j ==> for the movement from 1 col to another. 
# def knapsackTabulation(value, weight,TV,WC,i,j, lookup= {}):
#     dp =[[0]*(WC+1) for i in range(len(value))]
#     
#     for loop column movement:
#         for loop row movement:
#             
#             if weight at jth location is less than weight at ith location in weight array:
#                 
#                 the value at i and j in table = value at i-1 and j
#                 
#             else weight at jth location is equal to or higher than weight at ith location in weight array:
#             
#                 max(value[i]+value at i-1 and j-Weight at i location in weight array, value at i-1 and jth location)                
# =============================================================================
    

def knapsackTabulation(value, weight,TV,WC,i,j):
    dp =[[0]*(WC+1) for i in range(len(value))]
    
    if WC == 0:
        return 0
    elif WC>= sum(weight):
        return sum(value)
    for i in range(len(value)):
        for j in range(WC+1):
            
            if j < weight[i]:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j]= max(value[i]+dp[i-1][j-weight[i]], dp[i-1][j])
                
    return dp[-1][-1]
    
    
print("===================================>")
value = [60, 100, 120]
weight = [10, 20, 30]
WC = 50
print(knapsackTabulation(value, weight,TV=0,WC=WC,i=0, j = 0))
print("===================================>")
value = [ 20, 30,15,25,10]
weight = [ 6,13,5,10,3]
WC = 20
print(knapsackTabulation(value, weight,TV=0,WC=WC,i=0, j = 0))
