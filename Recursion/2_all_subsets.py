# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 20:36:27 2021

@author: Luv Verma
"""
def AllSubsetsWay1(arr, orig_arr, i, list1 ):
    
    if i == len(orig_arr):
        print(list1)
        print("arr",arr)
        if arr not in list1:
            list1.append(arr)
        return list1
    for kk in range(len(orig_arr)+1):
        AllSubsetsWay1(orig_arr[:kk], orig_arr, i+1, list1 )

def getsubsequenceRecursive(orig_arr):
    sub = []
    def AllSubsetsWay2(orig_arr, i,list1):
        # when the pointer i reaches the end, 
        #push the subsequence then into an array.
        if i == len(orig_arr):  
            #print(sub)
            #print("arr",arr)
            #if arr not in list1:
            sub.append(list1)
        else:
            # twice. once we add the current element to subsequence 
            # and once we dont as shown in the recursion tree. 
            # in both cases, the index should move. 
            # for example take the 1st element or do not take the first element. 
            #that will create two branches
            AllSubsetsWay2(orig_arr, i+1, list1+[orig_arr[i]] )
            AllSubsetsWay2(orig_arr, i+1, list1 )
    AllSubsetsWay2(orig_arr, 0,[])
    return sub


#=======================>
def getsubsequenceIterative(arr):
    # right off the bat, append an empty set. 
    
    list2 = []
    list2.append([]) # newlist will be: [[], ...............................]
    
    # go to first element in arr i.e 1 for [1,2,3]
    # go through all the elements in new list and add 1 to whatever there is already and create and 
    # append new element. 
    # newlist will be: [[], [1], ...............................]
    
    # adding 2, the newlist will become. 
    # newlist will be: [[], [1],[2],[1,2], ...............................]
    
    # every time we are doubling the number of subsets. from 1 to 2 to 4 to 8. 
    # we double everytime and do it n times (where n is the length of array), so the time complexity is: (O(n*2^n)) 
    # very high time complexity: (O(n*2^n)) ==> how to reduce this?    
    for i in range(len(arr)):
        print("i",i)
        print("list2",list2)
        for j in list2:
            
            if j is not None:
                print("j, arr[i]",j, arr[i])
                kk = j+[arr[i]]
                
                list2 = list2+[kk]
                print("kk, list2",kk, list2)
            #print("list1", list1)
    return list2
            
        
        
    
    
arr = [1,2,3]
i = 0
list1 = []
#AllSubsetsWay1(arr, orig_arr, i, list1 )
#getsubsequenceRecursive(arr)
getsubsequenceIterative(arr)
