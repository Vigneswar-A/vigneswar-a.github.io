# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        
        def compute_height(node):
            if node is None:
                return 0
            node.height = max(compute_height(node.left), compute_height(node.right))+1
            return node.height

        compute_height(root)
        queue = deque([root])
        res = {}
        distance = -1
        while queue:
            level = []
            max_height = 0
            distance += 1
            for _ in range(len(queue)):
                node = queue.popleft()
                if node is None:
                    continue
                level.append(node.left)
                level.append(node.right)
            queue.extend(level)
            heights = sorted(node.height for node in level if node is not None)
            if heights:
                for node in level:
                    if node is None:
                        continue
                    if node.height == heights[-1]:
                        res[node.val] = (heights[-2]+distance) if len(heights) > 1 else distance
                    else:
                        res[node.val] = heights[-1]+distance

        return [res[q] for q in queries]

            
            
                
                
                
        
            
            
          
            
            
            
                
        