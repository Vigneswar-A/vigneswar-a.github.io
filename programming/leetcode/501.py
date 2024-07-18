# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        counts = Counter()
        
        stack = [root]
        while stack:
            node = stack.pop()
            if node is None: continue
            counts[node.val] += 1
            stack.append(node.left)
            stack.append(node.right)
        
        modefreq = max(counts.values())
        return [i for i,c in counts.items() if c == modefreq]