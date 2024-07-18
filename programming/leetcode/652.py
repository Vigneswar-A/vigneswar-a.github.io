# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        
        
        subtrees = defaultdict(lambda : [None, 0])
        
        def get_sub_tree(node):
            if node is None:
                return '()'
            
            return str(node.val) + '(' + get_sub_tree(node.left) + get_sub_tree(node.right) + ')'
        
        stack = [root]
        while stack:
            node  = stack.pop()
            if node is None:
                continue
            subtrees[get_sub_tree(node)][0] = node
            subtrees[get_sub_tree(node)][1] += 1
    
            
                                             
                
            stack.append(node.left)
            stack.append(node.right)
            
        
        return [node for node ,count in subtrees.values() if count>1]
            
        