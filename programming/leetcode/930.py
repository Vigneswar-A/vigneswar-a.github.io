# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    @cache
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        if n == 0:
            return []
        elif n == 1:
            return [TreeNode()]
        
        res = []
        for left_node_count in range(1, n):
            right_node_count = n-left_node_count-1
            for left in self.allPossibleFBT(left_node_count):
                for right in self.allPossibleFBT(right_node_count):
                    res.append(TreeNode(0, left, right))
        return res
                    
                    
                
                
            
        
            
            
                
                                     
                                      
                
                
        