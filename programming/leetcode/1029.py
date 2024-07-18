# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        res = defaultdict(list)
        temp = defaultdict(list)
        queue = deque([(root,0)])
        
        while queue:
            temp.clear()
            for _ in range(len(queue)):
                node,x = queue.popleft()
                if not node:
                    continue

                temp[x].append(node.val)
                queue.append((node.right, x+1))    
                queue.append((node.left, x-1))
            
            for k,v in temp.items():
                res[k].extend(sorted(v))
            
            
        converted = {}
        for k,v in res.items():
            converted[tuple(v)] = k
            
        return sorted(converted, key = converted.get)
        