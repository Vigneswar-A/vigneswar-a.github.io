# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        maxlevel = 1
        maxans = -inf
        level = 1
        queue = deque([root])
        while queue:
            res = 0
            for _ in range(len(queue)):
                node = queue.popleft()
               
                     
                res += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if res > maxans:
                maxlevel = level
                maxans = res
            level += 1
            
        return maxlevel
             
                
                
            
        