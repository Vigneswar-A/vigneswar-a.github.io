# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        
        sums = Counter()
        def subtree_sum(root):
            if not root:
                return 0
            total = subtree_sum(root.left)+subtree_sum(root.right)+root.val
            sums[total] += 1
            return total
            
        subtree_sum(root)
        
        max_count = max(sums.values())
        return [i for i,j in sums.items() if j == max_count]
        
        