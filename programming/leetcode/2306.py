# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        
        child_map = defaultdict(list)
        non_root_nodes = set()
        for p,c,l in descriptions:
            child_map[p].append((c, l))
           
            non_root_nodes.add(c)
            
        for node in child_map:
            if node not in non_root_nodes:
                root = node
                break
                
        def build(node):
            for child, left in child_map[node.val]:
                if left:
                    node.left = TreeNode(child)
                    build(node.left)
                else:
                    node.right = TreeNode(child)
                    build(node.right)
            
        root = TreeNode(root)
        build(root)
        return root
                    
                   
            
            
            
        