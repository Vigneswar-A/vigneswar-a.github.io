# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        
        
        stack = [(root, None)]
        
        while stack:
            node, parent = stack.pop()
            node.parent = parent
            
            if node.left:
                stack.append((node.left, node))
                
            if node.right:
                stack.append((node.right, node))
                
        
        visited = set()
        queue = deque([target])
        for _ in range(k):
            for _ in range(len(queue)):
                node = queue.popleft()
                visited.add(node)
                for adj in [node.parent, node.left, node.right]:
                    if adj and adj not in visited:
                        queue.append(adj)
        
        return [node.val for node in queue]
        