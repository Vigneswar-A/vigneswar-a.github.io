# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        i = 0
        leaves = set()
        adjacency = defaultdict(set)
        def traverse(node):
            nonlocal i
            if node is None:
                return 
            node.val = i
            i += 1
            if node.left:
                traverse(node.left)
                adjacency[node.val].add(node.left.val)
                adjacency[node.left.val].add(node.val)
                
                
            if node.right:
                traverse(node.right)
                adjacency[node.val].add(node.right.val)
                adjacency[node.right.val].add(node.val)
            if node.left is None and node.right is None:
                
                leaves.add(node.val)
        traverse(root)
        print(leaves)
        print(adjacency)
        def dfs(node, dist=0):
            if dist >= distance:
                return 0
            
                
            
            
            res = 0
            visited.add(node)
            for adj in adjacency[node]:
                if adj in visited:
                    continue
                
                if adj in leaves:
                    res += 1
                else:
                    res += dfs(adj, dist+1)
           
                
            return res
        
        ans = 0
        for node in leaves:
            visited = set()
            ans += dfs(node)
        return ans//2
        
            
                



           
                
        
           
            
            
        