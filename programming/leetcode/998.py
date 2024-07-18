# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

TreeNode.__repr__ = lambda self : str(self.val)
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        
        queue = deque([root])
        flag = False
        while queue:
            node = queue.popleft()

            if node is None:
                flag = True
                continue
            
            if flag:
                return False

            queue.append(node.left)
            queue.append(node.right)


        return True
        
                    
            
        