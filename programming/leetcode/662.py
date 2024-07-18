# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        queue = deque([(root, 1)])
        ans = 0
        
        while queue:
            left = inf
            right = -inf
            for _ in range(len(queue)):
                node,x = queue.popleft()
                if node.left:
                    queue.append((node.left, 2*x-1))
                if node.right:
                    queue.append((node.right, 2*x))
                left = min(left, x)
                right = max(right, x)
            ans = max(ans, right-left+1)
            
        return ans
            