class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return
        queue,res=collections.deque([root]),[]
        while queue:
            temp=[]
            for i in range(len(queue)):
                node=queue.popleft()
                temp.append(node.val)
                if node.left:
                    queue.append(node.left)
                if  node.right:
                    queue.append(node.right)
                
            res.append(temp)
            
        return res