
"""
Search A Linked List With Jump References
Given a singly linked list with jump references annotate each list item's order field with its position in a "jump order traversal".

The jump pointer jumps to any random node in the linked list.

A "jump first" traversal is an iteration of the list giving priority to following jump pointers first before following next pointers.

The first node in the list is position 1 in the traversal.

Example:
Input:
                  ------------
                 |            |
                 ˅            |
Node{'a'} -> Node{'b'} -> Node{'c'} -> Node{'d'} -> X
   |             ^ |                       ^
   |             | |                       |
    -------------   -----------------------

Resulting Jump Order:
| Jump Order |   Node    |
| ---------- | --------- |
| 1          | Node{'a'} |
| 2          | Node{'b'} |
| 3          | Node{'d'} |
| 4          | Node{'c'} |

(Detailed) Explanation:
1.) We visit the head node first, Node{'a'}.
2.) We can follow the .next pointer or the .jump pointer, this is "jump first" so we follow the jump pointer
3.) We arrive at Node{'b'}
4.) Node{'b'} has a jump pointer so we follow it
5.) We arrive at Node{'d'}
6.) Node{'d'} has no jump pointer and no next pointer, so now we conceptually return control to Node{'b'} (where we came from)
7.) Node{'b'} already followed .jump, we follow .next
8.) We arrive at Node{'c'}
9.) Node{'c'}.jump goes to Node{'b'} (already visited), Node{'c'}.next goes to Node{'d'} (already visited)
10.) Control goes back to Node{'b'} (where we came from from the .next pointer)
11.) Node{'b'} already followed .jump and .next, we return to Node{'a'} (where we came from)
12.) Node{'a'} already followed its .jump pointer, Node{'a'}.next is Node{'b'} (already visited)
13.) Node{'a'} can go nowhere, we stop
"""    
    
class Solution: 
    
    def SetJumpOrder(self, Node, head):
        
        IntegerOrder = 0
        self.SetJumpOrderHelper(head, IntegerOrder)
        
    def SetJumpOrderHelper(self, node, IntegerOrder):
        
        if (node.val == None or node.val !=-1):
            '''
            If the above condition is true, 
            we will not process the node. We will return. 
            '''
            
            return
        
        # in recursive case, the work is to set order in the node. 
        
        node.val = IntegerOrder
        IntegerOrder = IntegerOrder+1
        
        self.SetJumpOrderHelper(node.jump, IntegerOrder)
        self.SetJumpOrderHelper(node.next, IntegerOrder)
    
