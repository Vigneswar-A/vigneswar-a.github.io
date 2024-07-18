# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestKValues(self, root: Optional[TreeNode], target: float, k: int) -> List[int]:
        
        heap = []
        stack = [root]
        while stack:
            node = stack.pop()
            if node is None:
                continue
            heappush(heap, (abs(node.val - target), node.val))
            stack.append(node.left)
            stack.append(node.right)
        return [arr[1] for arr in nsmallest(k, heap)]
