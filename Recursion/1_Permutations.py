# -*- coding: utf-8 -*-
"""
Created on Sun Oct  3 01:01:57 2021

@author: Luv Verma
"""
"""
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
"""
#===============================================>
def get_permutations(arr):
    if len(arr) == 0:
        return [arr]
    else:
        permutations = []
        for i in range(len(arr)):
            if arr[i] not in arr[:i]:
                remaining = get_permutations(arr[:i]+arr[i+1:])
                for permutation in remaining:
                    permutation.append(arr[i])
                    permutations.append(permutation)
        return permutations
#===============================================>

# the swap way below is more used. 
def main(arr):
    n = len(arr)
    permutations = []   
    
    get_permutationsWay2(arr, 0, n-1, permutations)
    return permutations
    
def get_permutationsWay2(arr, left, right, permutations):  
    if (left == right):
        # if index left reaches the last position, i.e equivalent to right. 
        permutations.append(arr[:])
    else:
        for i in range(left, right+1):
            swap(arr, left, i)
            get_permutationsWay2(arr, left+1, right, permutations)
            # why swapping again is required?
            swap(arr, left, i)

def swap(arr, i,j):
    arr[i], arr[j] = arr[j], arr[i]
            
            
    
    
    
arr = [1,2,3]
#arr = "ABC"
#print(get_permutations(arr))
print(main(arr))