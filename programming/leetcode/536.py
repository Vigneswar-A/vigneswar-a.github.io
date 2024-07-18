# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def str2tree(self, s: str) -> Optional[TreeNode]:
        
        
        s = list(filter(None, re.split(r'(\(|\))', s)))
        stack = []
        parentmap = {}
        
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            elif s[i] == ')':
                parentmap[stack.pop()] = i
                

        def build(left=0, right=len(s)-1):
            if left > right:
                return None
            if left == right:
                return TreeNode(s[left])
            root = TreeNode(s[left])
            root.left = build(left+2, parentmap[left+1]-1)
            root.right = build(parentmap[left+1]+2, right-1)
            return root
        
        return build()
            
            
                
                
                
                
            
                
                

        
            
            