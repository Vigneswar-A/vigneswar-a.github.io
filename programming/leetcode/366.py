# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        heights = {}
        res = defaultdict(list)
        
        def get_height(node):
            if not node:
                return 0
                
            heights[node] = max(get_height(node.left), get_height(node.right)) + 1
            res[heights[node]].append(node.val)
            
            return heights[node]
            
            
        get_height(root)
        
        return res.values()
                
            
            
                
            
            
                
            
                
            
                
                
            
                
        