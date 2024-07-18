# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        
        @cache
        def find(node, target):
            if node is None:
                return False
            if node.val == target:
                return True
            return find(node.left, target) or find(node.right, target)
        
        def lowest_common_ancestor(node, a, b):
            if node is None:
                return
            if find(node.left, a) and find(node.left, b):
                return lowest_common_ancestor(node.left, a, b)
            elif find(node.right, a) and find(node.right, b):
                return lowest_common_ancestor(node.right, a, b)
            else:
                return node.val
            
        def path_from_root(node, target, path=[]):
            if find(node.right, target):
                path.append('R')
                path_from_root(node.right, target, path)
            elif find(node.left, target):
                path.append('L')
                path_from_root(node.left, target, path)     
            return path
        
        lsa = lowest_common_ancestor(root, startValue, destValue)
        root_to_start = path_from_root(root, startValue, [])
        root_to_dest = path_from_root(root, destValue, [])
        root_to_lsa = path_from_root(root, lsa, [])
        
        
        
        
        
        return ''.join((len(root_to_start)-len(root_to_lsa))*['U']+root_to_dest[len(root_to_lsa):])
            
                

            
        
            
            
        