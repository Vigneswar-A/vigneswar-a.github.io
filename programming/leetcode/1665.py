"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def diameter(self, root: 'Node') -> int:
       
        @cache
        def length(node):
            if node is None:
                return 0
            return max((length(child) for child in node.children), default=0)+1
        
        
        sub = []
        for child in root.children:
            sub.append(length(child))
        sub.sort(reverse=1)
        res = sum(sub[:2:])
        return max(res, max((self.diameter(child) for child in root.children), default=0))
            
            
        
       