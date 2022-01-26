"""
Given an array words of words return the distance between the nearest repeated entries.

If no entry is repeated return -1.

Example 1:
Input:
[
  "This",
  "is",
  "a",
  "sentence",
  "with",
  "is",
  "repeated",
  "then",
  "repeated"
]
Output: 2
Explanation: "repeated" (index 6) and "repeated" (index 8) are 2 positions away.

Example 2:
Input:
[
  "This",
  "is",
  "a"
]
Output: -1
Explanation: There are no repeated entries.
"""

class Solution: 
    
    def nearest_repeated_entry(self, Input):
        
        return self.nearest_repeated_entry_helper(Input)
        
    def nearest_repeated_entry_helper(self,Input):
        dict1 = {}
        for i,k in enumerate(Input):
            print(i,k)
            if k not in dict1:
                dict1[k] = [i]
            else:
                dict1[k].append(i)

        return dict1
            
s = Solution()
Input=["This","is","a",
  "sentence",
  "with",
  "is",
  "repeated",
  "then",
  "repeated"]
print(s.nearest_repeated_entry(Input))
            
    
    
    