# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def update_child_sum(node):
            if node is None:
                return 
            node.child_sum = 0
            if node.left:
                node.child_sum += node.left.val
                update_child_sum(node.left)
                node.left.parent = node
            if node.right:
                node.child_sum += node.right.val
                update_child_sum(node.right)
                node.right.parent = node
            
        update_child_sum(root)
        queue = deque([root])
        while queue:
            level = []
            level_sum = 0
            for _ in range(len(queue)):
                node = queue.popleft()
                if node is None:
                    continue
                level_sum += node.val
                level.append(node)
                queue.append(node.left)
                queue.append(node.right)
            for node in level:
                if node == root:
                    node.val = 0
                else:
                    node.val = level_sum-node.parent.child_sum
              
        return root
            
            
        
        