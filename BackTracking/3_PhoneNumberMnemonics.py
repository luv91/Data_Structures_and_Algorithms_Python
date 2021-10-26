"""
Phone Number Mnemonics
Given a string digits representing a phone number, 
return all possible character arrangements that can result 
from the number.

Each digit maps like so:
2 -> "a" || "b" || "c"
3 -> "d" || "e" || "f"
4 -> "g" || "h" || "i"
5 -> "j" || "k" || "l"
6 -> "m" || "n" || "o"
7 -> "p" || "q" || "r" || "s"
8 -> "t" || "u" || "v"
9 -> "w" || "x" || "y" || "z"

Example 1:
Input: "43"
Output: ["gd","ge","gf","hd","he","hf","id","ie","if"]

Example 2:
Input: "239"
Output:
[
  "adw","adx","ady","adz",
  "aew","aex","aey","aez",
  "afw","afx","afy","afz",
  "bdw","bdx","bdy","bdz",
  "bew","bex","bey","bez",
  "bfw","bfx","bfy","bfz",
  "cdw","cdx","cdy","cdz",
  "cew","cex","cey","cez",
  "cfw","cfx","cfy","cfz"
]
Constraints:
s will only digits between 2 and 9
2 <= n <= 10 (constraint on length of string)
"""
class Solution: 
    
    digits_to_letters = [
        "",      # 0
        "",      # 1
        "abc",   # 2
        "def",   # 3
        "gh",   # 4
        "jk",   # 5
        "mn",   # 6
        "pq",  # 7
        "tu",   # 8
        "wx"   # 9
        ]
    
    def letterCombinations(self, digits):
        '''
        :type digits: str
        :rtype: list of str
        '''
        
        # when input string is empty. 
        if len(digits) == 0:
            return []
        mnemonics = []
        self.explore_combinations(0,digits,"", mnemonics)
        return mnemonics
    
    def explore_combinations(self,index_digit, digits,partial_mnemonic,result):
        
        if index_digit == len(digits):
            #print(result)
            result.append(partial_mnemonic)
            return
        list_digits = list(digits)
        list_digits = [int(i) for i in list_digits]
        print(list_digits)
        letters = Solution.digits_to_letters[list_digits[index_digit]]
        print("letters", letters)
        for kk in letters: 
            partial_mnemonic = partial_mnemonic+kk
            
            self.explore_combinations(index_digit+1, digits,partial_mnemonic,result)
            
            partial_mnemonic = partial_mnemonic[:-1]
            
s = Solution()
        
print(s.letterCombinations("23"))
        
        
        