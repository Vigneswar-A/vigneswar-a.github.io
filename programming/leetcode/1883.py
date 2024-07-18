# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDistance(self, root: Optional[TreeNode], p: int, q: int) -> int:
        
        adjacency = defaultdict(list)
        
        def dfs(node):
            if node is None:
                return 
            
            if node.left:
                adjacency[node.left.val].append(node.val)
                adjacency[node.val].append(node.left.val)
                
            if node.right:
                adjacency[node.right.val].append(node.val)
                adjacency[node.val].append(node.right.val)
                
            dfs(node.left)
            dfs(node.right)
            
        dfs(root)
        queue = deque([p])
        dist = 0
        visited = set()
        
        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                if node == q:
                    return dist
                for adj in adjacency[node]:
                    if adj not in visited:
                        visited.add(adj)
                        queue.append(adj)
            dist += 1
            
        return 0
            
                        
                
            
            
            
        
                
            
            
        