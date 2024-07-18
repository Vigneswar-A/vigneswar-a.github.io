# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def correctBinaryTree(self, root: TreeNode) -> TreeNode:
        
        queue = deque([(None, root)])
        
        while queue:
            hashset = set()
            for _ in range(len(queue)):
                parent, node = queue.popleft()
                if node is None:
                    continue
                if node and node.right in hashset:
                    if parent.left == node:
                        parent.left = None
                    else:
                        parent.right = None
                    break
                hashset.add(node)
                queue.append((node, node.right))
                queue.append((node, node.left))
                
                
        return root
        