# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findNearestRightNode(self, root: TreeNode, u: TreeNode) -> Optional[TreeNode]:
        
        queue = deque([root])
        found = False
        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                if found:
                    return node
                if node == u:
                    found = True
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if found:
                return None
            
        
    
                
            
                
        
            
                
        
                
            
        