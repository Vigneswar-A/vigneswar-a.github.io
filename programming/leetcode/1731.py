# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        
        queue = deque([root])
        mod = 1
        while queue:
            prev = None
            for i in range(len(queue)):
                if queue[0] is None:
                    queue.popleft()
                    continue
                if prev is None:
                    if queue[0].val%2 != mod:
                        return False
                else:
                    if mod%2 == 0 and (queue[0].val%2 != mod or prev.val <= queue[0].val):
                        return False
                    elif mod%2 and (queue[0].val%2 != mod or prev.val >= queue[0].val):
                        return False
                prev = queue.popleft()
                queue.extend([prev.left, prev.right])
            mod = not mod
                                
        return True
                
        