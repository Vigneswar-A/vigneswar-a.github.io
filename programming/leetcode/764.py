"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        
        levels = defaultdict(list)
        def traverse(node = root, depth=0):
            if node is None:
                return
            levels[depth].append(node.val)
            for childnode in node.children:
                traverse(childnode, depth+1)
        traverse()
        return [*levels.values()]
        