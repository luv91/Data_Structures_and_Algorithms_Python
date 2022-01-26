# -*- coding: utf-8 -*-
"""
Created on Wed Jan 26 12:29:00 2022

@author: Luv Verma
"""

# https://www.udemy.com/course/learn-recursion/learn/lecture/23974312#overview

# comb is current list, 
# combs is a final combination. 
def weight_comb_Self(arr,mW, i = 0, comb =[], combs = []):
    
# =============================================================================
#     if i == len(arr) or mW==0:
#         combs.append(comb.copy())
# =============================================================================
        #return
        
    # order of base cases is important. 
    # because if we switch, the case where mw becomes negative at 4th
    #index will be copied into combs
    if mW < 0:
        return
    elif i == len(arr):
        # comb.copy() is important here.. if you just append comb, it will be an issue
        combs.append(comb.copy())
        

    else:
        print(i,mW,combs)
        comb.append(arr[i])
        weight_comb_Self(arr,mW-arr[i], i+1)
        comb.pop()
        weight_comb_Self(arr,mW, i+1)
    #print("combs",combs)   
    return combs
        
        
    
    


weights =[4,7,2,1]
mW = 7
#print(weight_comb_Self(weights,mW))


def weight_comb(arr,mW, i, comb, combs):
    
# =============================================================================
#     if i == len(arr) or mW==0:
#         combs.append(comb.copy())
# =============================================================================
        #return
        
    # order of base cases is important. 
    # because if we switch, the case where mw becomes negative at 4th
    #index will be copied into combs
    if mW < 0:
        return
    elif i == len(arr):
        # comb.copy() is important here.. if you just append comb, it will be an issue
        combs.append(comb.copy())
        

    else:
        print(i,mW,combs)
        comb.append(arr[i])
        weight_comb(arr,mW-arr[i], i+1, comb, combs)
        comb.pop()
        weight_comb(arr,mW, i+1, comb, combs)
    #print("combs",combs)   
    
def getCombs(weights,maxWeight):
    combs = []
    weight_comb(weights,maxWeight, 0, [], combs)
    return combs
            
        
    
    


weights =[4,7,2,1]
mW = 7
print(getCombs(weights,mW))
#print(weight_comb_Self(weights,mW))