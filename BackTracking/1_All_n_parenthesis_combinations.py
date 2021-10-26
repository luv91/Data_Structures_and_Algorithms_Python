# example 8p9. cracking the coding interview, Backtracking, recursion and DP
"""
Generate All Strings With n Matched Parentheses
Given an integer value n, return all possible strings of n matched parentheses.

Example 1:
Input: 1
Output: ["()"]

Example 2:
Input: 2
Output: ["(())","()()"]

Example 3:
Input: 3
Output:
[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
"""
class Solution: 
    def generateParenthesis(self, numPairs):
        
        result = []
        self.generate(numPairs, numPairs, "", result)
        return result
    
    '''
        The recursion has bottomed out.

        We have used all left and right parens necessary within constraints up
        to this point. Therefore, the answer we add will be a valid paren string.
      
        We can add this answer and then backtrack so the previous call can exhaust
        more possibilities and express more answers...and then return to its caller,
        etc. etc.

        Yeah...this is what backtracking is all about.
        '''
        
    def generate(self, num_left_paren_needed,
                 num_right_paren_needed,
                 paren_string_in_progress,
                 result):
        
        if (num_left_paren_needed == 0 and num_right_paren_needed== 0):
            result.append(paren_string_in_progress)
            
            return 
        
        '''
        At each frame of the recursion we have 2 things we can do:

        1.) Insert a left parenthesis
        2.) Insert a right parenthesis

        These represent all of the possibilities of paths we can take from this
        respective call. The path that we can take all depends on the state coming
        into this call.
        '''

        '''
        Can we insert a left parenthesis? Only if we have lefts remaining to insert
        at this point in the recursion
        '''
        if (num_left_paren_needed > 0):
            '''
            numLeftParensNeeded - 1 ->       We are using a left paren
            numRightParensNeeded ->          We did not use a right paren
            parenStringInProgress + "(" ->   We append a left paren to the string in progress
            result ->                        Just pass the result list along for the next call to use
            '''
            self.generate(num_left_paren_needed-1,
                 num_right_paren_needed,
                 paren_string_in_progress+"(",
                 result)
            
        '''
        Can we insert a right parenthesis? Only if the number of left parens needed
        is less than then number of right parens needed.
      
        This means that there are open left parenthesis to close OTHERWISE WE CANNOT
        USE A RIGHT TO CLOSE ANYTHING. We would lose balance.
        '''
        
        if (num_left_paren_needed <num_right_paren_needed):
            '''
            numLeftParensNeeded ->           We did not use a left paren
            numRightParensNeeded - 1 ->      We used a right paren
            parenStringInProgress + ")" ->   We append a right paren to the string in progress
            result ->                        Just pass the result list along for the next call to use
            '''
            self.generate(num_left_paren_needed,
                 num_right_paren_needed-1,
                 paren_string_in_progress+")",
                 result)
            
s = Solution()
print(s.generateParenthesis(3))