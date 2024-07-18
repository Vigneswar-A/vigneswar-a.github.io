"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def findRoot(self, tree: List['Node']) -> 'Node':
        
        degrees = Counter()
        
        for t in tree:
            degrees[t] += 0
            for child in t.children:
                degrees[child] += 1
                
        return [root for root,degree in degrees.items() if degree == 0][0]
        