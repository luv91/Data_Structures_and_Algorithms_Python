
'''
Leet code 20. Valid Parentheses

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.

Input: s = "()[]{}"
Output: true

Input: s = "([)]"
Output: false

Input: s = "{[]}"
Output: true
'''
# not very strong in logic, but gives solution because of python .get trick in hashmaps
class SolutionWay1: 
    
    def is_valid_parenthesis(self, input1):
        
        return self.is_valid_parenthesis_helper(input1)
        
    def is_valid_parenthesis_helper(self,input1):
        
        hash1 = {"(":")",
                 "{":"}",
                 "[":"]" }
        inv_hash = {v:k for k, v in hash1.items()}
        print("inv_hash", inv_hash)
        stack1 = []
        
        for key in input1:
            stack1.append(key)
            print("stack1",stack1)
            if stack1[-1] in inv_hash:
                
                #print("stack1[-1],hash1[stack1[-2]",stack1[-1],hash1[stack1[-2]])
                # I am taking the help of python 
                # here to overcome the logic issues.. 
                
                if stack1[-1] == hash1.get(stack1[-2]):
                    stack1.pop()
                    stack1.pop()
# =============================================================================
#                     if len(stack1) %2!= 0:
#                         return False
# =============================================================================
                    print("stack after popping",stack1)
        if len(stack1) == 0:
            return True
        
        return False
            
            
s1 = SolutionWay1()
#input1 = "()"
input1= "([)]"
print(s1.is_valid_parenthesis_helper(input1))  

#=====================================>
# logic is better. used elif statement and thus only 
# keys in hash1 are taken as an input..
class SolutionWay2: 
    
    def is_valid_parenthesis(self, input1):
        
        return self.is_valid_parenthesis_helper(input1)
        
    def is_valid_parenthesis_helper(self,input1):
        
        hash1 = {"(":")",
                 "{":"}",
                 "[":"]" }
        inv_hash = {v:k for k, v in hash1.items()}
        print("inv_hash", inv_hash)
        stack1 = []
        
        for key in input1:
            if key in hash1:
                stack1.append(key)
                print("stack1",stack1)
            elif key in inv_hash:
                
                #print("stack1[-1],hash1[stack1[-2]",stack1[-1],hash1[stack1[-2]])
                # I am taking the help of python 
                # here to overcome the logic issues.. 
                
                if key == hash1.get(stack1[-1]):
                    stack1.pop()
                    #stack1.pop()
# =============================================================================
#                     if len(stack1) %2!= 0:
#                         return False
# =============================================================================
                    print("stack after popping",stack1)
        if len(stack1) == 0:
            return True
        
        return False
            
            
s2= SolutionWay2()
#input1 = "()"
input1= "{([{}])}"
print(s2.is_valid_parenthesis_helper(input1))                 
            
        
        