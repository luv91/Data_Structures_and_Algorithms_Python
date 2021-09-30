# DP_1
# Find the maximum sum of a subsequence with no adjacent elements

# Given an array of positive numbers, 
# find the maximum sum of a subsequence with the constraint
#  that no 2 numbers in the sequence should be adjacent in the array. So 3 2 7 10 should return 13 (sum of 3 and 10) or 3 2 5 10 7 should return 15 (sum of 3, 5 and 7).Answer the question in most efficient way.

# Input : arr=[7,10,12,7,9,14]
#Output : is 33 i.e elements, 7+12+14 = 33

def find_max_sum(arr):
    i = 0
    sm = []
    while i < len(arr):
        if i == 0 or i == 1:
            sm.append(arr[i])
        else:
            max_sum = max(sm[i-1], sm[i-2]+arr[i])
            sm.append(max_sum)
        
        
        i = i+1

    print(sm) 
    return max_sum

arr = [7,10,12,7,9,14]
print(find_max_sum(arr))
    

