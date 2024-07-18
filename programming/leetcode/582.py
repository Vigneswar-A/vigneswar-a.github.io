class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        
        hashmap = defaultdict(list)
        
        for child,parent in zip(pid, ppid):
            hashmap[parent].append(child)
            
        queue = deque([kill])
        res = []
        while queue:
            node = queue.popleft()
            res.append(node)
            queue.extend(hashmap[node])
        
        return res
            