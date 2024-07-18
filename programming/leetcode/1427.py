# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        
        def get_list(root):
            stack = []
            node = root
            while stack or node:
                while node:
                    stack.append(node)
                    node = node.left
                node = stack.pop()
                yield node.val
                node = node.right
            
        
            
        res = []
        list1 = [*get_list(root1)]
        list2 = [*get_list(root2)]
        
        i = j = 0
        while i < len(list1) and j < len(list2):
            if list1[i] < list2[j]:
                res.append(list1[i])
                i += 1
            else:
                res.append(list2[j])
                j += 1
                
        for i in range(i, len(list1)):
            res.append(list1[i])
            
        for j in range(j, len(list2)):
            res.append(list2[j])
            
        return res