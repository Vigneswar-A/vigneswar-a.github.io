class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        visited = set()
        stack = [start]
        
        while stack:
            node = stack.pop()
            if node in visited or node < 0 or node >= len(arr):
                continue
            visited.add(node)
            
            if arr[node] == 0:
                return True
            
            stack.append(node + arr[node])
            stack.append(node - arr[node])
            
        