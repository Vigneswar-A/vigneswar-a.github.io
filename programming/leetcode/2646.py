# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        
        res = []
        queue = deque([root])
        
        while queue:
            level_sum = 0
            for _ in range(len(queue)):
                node = queue.popleft()
                if node is None:
                    continue
                level_sum += node.val
                queue.append(node.left)
                queue.append(node.right)
            res.append(level_sum)
            
        res.sort(reverse=1)
        return res[k-1] if k < len(res) else -1
                