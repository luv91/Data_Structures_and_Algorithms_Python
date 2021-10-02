# -*- coding: utf-8 -*-
"""
Created on Thu Sep 30 23:07:19 2021

@author: Luv Verma
"""

'''
You are given an integer array coins representing coins of different 
denominations and an integer amount representing a total amount of money.

Return the number of combinations that make up that amount. 
If that amount of money cannot be made up by any combination 
of the coins, return 0.
You may assume that you have an infinite number of each kind of coin.

Example 1:
Input: amount = 5, coins = [1,2,5]
Output: 4
Explanation: there are four ways to make up the amount:
5=5
5=2+2+1
5=2+1+1+1
5=1+1+1+1+1
'''
# create a 1-d array, that gives the number of ways. 
# the indices of the array above is uptill the amount. 
# initializes from index 0 and that will have value of 1. 
# as it is our base case.

def num_ways(n, coins):
    
    ways = [0]*(n+1) # amount +1 because starting from index 0, it has to go to index 5. 
    ways[0] = 1
    for coin in coins:
        amount = 1
        while amount < len(ways):
            
            if coin<= amount:
                ways[amount] += ways[amount-coin]
                
            amount = amount+1
    print(ways)
    return ways[-1]


amount = 5
coins = [1,2,5]

num_ways(amount, coins)