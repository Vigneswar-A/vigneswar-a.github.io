"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        res = []
        def traverse(node):
            if node is None:
                return
            for childnode in node.children:
                traverse(childnode)
            res.append(node.val)
            
        traverse(root)
        return res
        