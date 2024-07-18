# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:return
        stack,res=collections.deque([root]),[]
        
        while stack:
            node=stack.popleft()
            if node.left:
                stack.appendleft(node.left)            
            if node.right:
                stack.appendleft(node.right)
            
            res.append(node.val)
        return res[::-1]
        