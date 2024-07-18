# Definition for a rope tree node.
# class RopeTreeNode(object):
#     def __init__(self, len=0, val="", left=None, right=None):
#         self.len = len
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getKthCharacter(self, root: Optional[object], k: int) -> str:
        
        def S(node):
            if node is None:
                return ""
            if node.len == 0:
                return node.val
            
            return S(node.left)+S(node.right)
        
        return S(root)[k-1]