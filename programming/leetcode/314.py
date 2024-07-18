# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        res = defaultdict(list)
        def travel(node, coord , depth):
            res[coord].append((depth,node.val))
            
            if node.left:
                travel(node.left , coord-1 , depth+1)
            
            if node.right:
                travel(node.right , coord+1 , depth+1)
                
        travel(root , 0 , 0)
        convert = {}
        for coord,List in res.items():
            convert[tuple(zip(*sorted(List, key = lambda arr:arr[0])))[1]] = coord

        return sorted(convert , key = convert.get)
            
    
            
            
        