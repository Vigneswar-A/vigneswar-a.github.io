# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        
        def build(l, r):
            if l > r:
                return None
            root_idx = max(range(l, r+1), key=nums.__getitem__)
            root = TreeNode(nums[root_idx])
            root.left = build(l, root_idx-1)
            root.right = build(root_idx+1, r)
            return root
        
        return build(0, len(nums)-1)