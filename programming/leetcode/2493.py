# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        queue = deque([root])
        isodd = True
        while queue:
            isodd = not isodd
            nodes = []
            vals = []
            for _ in range(len(queue)):
                node = queue.popleft()
                if isodd:    
                    nodes.append(node)
                    vals.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                    
            for i in range(len(nodes)):
                nodes[i].val = vals[-i-1]
                
        return root
                
            
                
        