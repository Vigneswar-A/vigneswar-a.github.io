# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        
        graph = defaultdict(list)
        
        stack = [root]
        while stack:
            node = stack.pop()
            if node.left:
                graph[node.val].append(node.left.val)
                graph[node.left.val].append(node.val)
                stack.append(node.left)
            if node.right:
                graph[node.val].append(node.right.val)
                graph[node.right.val].append(node.val)
                stack.append(node.right)
                
        queue = deque([start])
        visited = set()
        dist = -1
        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                visited.add(node)
                for adj in graph[node]:
                    if adj not in visited:
                        queue.append(adj)
            dist += 1
            
            
        return dist
                
        
            
                
        