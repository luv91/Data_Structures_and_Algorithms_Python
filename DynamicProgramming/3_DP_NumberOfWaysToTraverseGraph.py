# -*- coding: utf-8 -*-
"""
Created on Sat Oct  2 19:29:13 2021

@author: Luv Verma
"""
"""
Number of ways to Traverse Graph:
    You are given two positive integers representing the width and height
    of a grid-shaped ,r ectangular graph.
    
    Write a function that returns the number of ways to reach the bottom right corner
    of the graph when starting at the toip left corner. Each move you 
    take must either go down or right. In other words, you can never move
    up or left in the graph. 
    
    For example, given the graph wuith width = 2, height = 3, there are three ways
    to ereach to the bottom right corner when starting at the top left corner:
        _ _
       |_|_|
       |_|_|
       |_|_|
       
       above there are three rows, which is height and 2 columns, which is width
       answer is 3. 
       1. Down, Down, right
       2. Right, Down, Down
       3. Down, Right, Down
"""

# Way 1: Solve using recursion
# Time complexity of recursion method is: O(2**(row+col)); Very costly and bad solution
# how would the recursive tree look like?
def count_ways_graphs(row,col):
    if row == 1 or col == 1:
        #count = 1
        return 1
  
    return count_ways_graphs(row-1,col) +count_ways_graphs(row,col-1)

#============================================>
# Way 2: Solve using DP: Start from the beginning and work the way to the end. 
# two pointers to keep track of the row and the columns
# pointer 1 will move over the height or the rows. 
# pointer 2 will move over the width or the columns
# this solution will be O(row*col)
# =============================================================================
# def count_ways_graphs_way2(row,col):
#     count_way2 = [[0]*col]*row
#     for i in range(col):
#         for j in range(row):
#             if i == 0:
#                 print("i,j",i,j)
#                 
#                 count_way2[j][i]=1
#                 print(count_way2)
#             elif j == 0:
#                 count_way2[j][i]=1
#                 
#             
#             else:
#                 print("i,j inside else",i,j)
#                 print("count_way2 inside else",count_way2)
#                 count_way2[j][i]= (count_way2[j-1][i]+count_way2[j][i-1])
#     return count_way2
# =============================================================================
#========================================>
# this piece of code way2 works but has problem as the way count_Way2 is initialized is wrong. 
def count_ways_graphs_way2(row,col):
    #count_way2=[[1,2],[3,4],[5,6]]
    count_way2 = [[0]*col]*row
    for i in range(row):
        print(count_way2[i][0])
        
    for j in range(col):
        print(count_way2[0][j])
        
    for i in range(row):
        for j in range(col):
             if i == 0 or j == 0:
                 count_way2[i][j]=1
                 print(count_way2)
             else:
                 count_way2[i][j] = count_way2[i-1][j]+count_way2[i][j-1]
                 print("count_way2 inside else",count_way2)
    return count_way2[row-1][col-1]
                 
#========================================>  
# same as way2 but list comprehension initialization, as above is giving wrong solution.           
def count_ways_graphs_way3(row,col):
    #count_ways3 = [[0]*col]*row ==> this is shitty, do not use this. 
    count_ways3 = [[0 for _ in range(col)] for _ in range(row)]
    #print(count_ways3)
    for row_idx in range(0, row):
        for col_idx in range(0, col):
            if row_idx == 0 or col_idx == 0:
                count_ways3[row_idx][col_idx] = 1
            else:
                ways_left = count_ways3[row_idx][col_idx-1]
                ways_up = count_ways3[row_idx-1][col_idx]
                
                count_ways3[row_idx][col_idx] = ways_up+ways_left
                #count_ways3[row_idx][col_idx] = count_ways3[row_idx][col_idx-1]+count_ways3[row_idx-1][col_idx]
    print(count_ways3)
#========================================>  
# Way 4 ==> Recursion+ memoization  also called as top-down approach (Chapter -8, DP and recursion, Cracking the coding interview book )
def count_ways_graphs_way4(row,col):
    memo = {} # create a dictionary
    # dictionary has key as a tuple pair with both row and col. ; 
    #value of the key (row, col) pair is the value. 

    if (row,col) in list(memo.keys()): 
            return memo[(row,col)]
    if row == 1 or col == 1:
        #count = 1
        f = 1
    else:
        f = count_ways_graphs_way4(row-1,col) +count_ways_graphs_way4(row,col-1)
    memo[(row,col)]=f  
    return f

    
        
#def test_case_1(self):
width = 4
height = 3
#expected = 10
print(count_ways_graphs(height,width))
print(count_ways_graphs_way2(height,width))
print(count_ways_graphs_way3(height,width))
print(count_ways_graphs_way4(height,width))
    #self.assertEqual(actual, expected)
        