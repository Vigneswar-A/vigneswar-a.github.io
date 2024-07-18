# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        to_delete = set(to_delete)
        trees = [root]
        def delete(node, parent):
            if node is None:
                return 
            
            if node.val in to_delete:
               
                to_delete.remove(node.val)
                if parent and parent.left == node:
                    parent.left = None
                elif parent:
                    parent.right = None
                else:
                    trees.remove(node)
                trees.append(node.left)
                trees.append(node.right)
            else:
                delete(node.left, node)
                delete(node.right, node)
        
        while to_delete:
            
            
            
            for node in trees.copy():
                delete(node, None)
                
        return filter(None, trees)
            
        
               
            
                
                
               
            
            
            
            
        