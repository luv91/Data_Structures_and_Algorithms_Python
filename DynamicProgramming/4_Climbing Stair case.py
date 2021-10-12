# -*- coding: utf-8 -*-
"""
Created on Sun Oct  3 00:34:56 2021

@author: Luv Verma
"""

# Leetcode => 70 climbing stairs
"""
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
=========>
Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
#=================>
INput n = 10
possible Steps = [2,4,5,8]
output = 11. 
"""

# ==============>
# Solution 1: Recursive
# think of a recursive tree.. 
# the way to reach 10 is equal to 4 recursion trees. 
# i.e the way to reach(10-2); the way to reach (10-4); (10-5) and (10-8)
def ClimbingStairs(n, possibleSteps= [2,4,5,8]):
    count = 0 
    if n == 0:
        
        return 1
    
    for steps in possibleSteps:
        if (n-steps)>=0:
            count += ClimbingStairs(n-steps)
    #print(count)
    return count

#==================================>
# Top-Down Dynamic Programming (or Memoization)
# Solution 2: To make recursion fast, we have to add some kind of lookup:
# if we are calling something which has already been called store that up in a lookup table. 
# so that it can be taken from the lookup table instead of calculating it again.     
# This one is correct. 
def ClimbingStairsWay2(n, possibleSteps, lookup):
    key = str(n)
    
    
    if key in lookup:
        return lookup[key]
    
    elif n == 0:
        lookup[key] = 1
        return lookup[key]
        # count = 1
    else:
        count = 0 
        for steps in possibleSteps:
            if (n-steps)>=0:
                count += ClimbingStairsWay2(n-steps,possibleSteps, lookup)
        lookup[key] = count
        return lookup[key]
# =============================================================================
#     print(count)
#     return count    
# =============================================================================
# Top-Down Dynamic Programming (or Memoization)
# Another Way: Less number of return statements
def ClimbingStairsWay3(n, possibleSteps, lookup):
    key = str(n)
    
    
    if key in lookup:
        return lookup[key]
    
    elif n == 0:
        count = 1
        
        # count = 1
    else:
        count = 0 
        for steps in possibleSteps:
            if (n-steps)>=0:
                count += ClimbingStairsWay3(n-steps,possibleSteps, lookup)
    lookup[key] = count
    return lookup[key]    
# =============================================================================
# Bottom- Up Dynamic Programming:   
# Recursive + Mmeoization solution (Wya 2) can be converted into 
# table based DP solution.     
def ClimbingStairsWay4(n, possibleSteps):
    dp = [0]*(n+1)
    dp[0] = 1
    #count = 0
    for i in range(1, len(dp)):
        count = 0
        for step in possibleSteps:
            if (i-step) >= 0:
                count +=dp[i-step]
                
        dp[i] = count
    return dp[n]

                
        
        



# =============================================================================
# # Solution Another Type: This problem can be solved similarly to coin problem. 
# # *** Very Important: Did not Work. 
# def ClimbingStairsWay2(n, possibleSteps= [2,4,5,8]):
#     ways = [0 for _ in range(n+1)]
#     #ways = [0]*(n+1) 
#     ways[0] = 1
#     for step in possibleSteps:
#         amount = 1
#         while amount < len(ways):
#             if step <= amount:
#                 ways[amount] +=ways[amount-step]
#             
#             amount= amount+1
#     print(ways)
#     return ways[-1]
# =============================================================================
            




possibleSteps = [2,4,5,8]
n=50
#print(ClimbingStairs(n))
lookup = {}
print(ClimbingStairsWay2(n,possibleSteps,lookup))
print(ClimbingStairsWay3(n,possibleSteps,lookup))
print(ClimbingStairsWay4(n, possibleSteps))
#ClimbingStairsWay2(n)