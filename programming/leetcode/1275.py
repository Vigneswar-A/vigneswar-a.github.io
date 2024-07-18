class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        
        parents = {}
        
        for node,(left,right) in enumerate(zip(leftChild, rightChild)):
            if left != -1 and left not in parents:
                parents[left] = node
            elif left != -1:
                return False
            
            if right != -1 and right not in parents:
                parents[right] = node
            elif right != -1:
                return False

        count = 0
        root = None
        for node in range(n):
            if node not in parents:
                count += 1
                root = node
            if count > 1:
                return False
            
        
        adj = defaultdict(list)
        for child,parent in parents.items():
            adj[parent].append(child)
            
        if root is None:
            return False

        stack = [root]
        visited = set()
        while stack:
            node = stack.pop()
            if node in visited:
                return False
            visited.add(node)
            stack.extend(adj[node])
        
        return len(visited) == n
            