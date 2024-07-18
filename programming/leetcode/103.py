# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        res = []
        
        queue = deque([root])
        i = 0
        
        while queue:
            temp = []
            i += 1
            for _ in range(len(queue)):
                node = queue.popleft()
                if node is None:
                    continue
                temp.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
            
            if i%2  == 0:
                temp.reverse()
            
            if temp:
                res.append(temp)
            
        return res
                
            
        
    
        