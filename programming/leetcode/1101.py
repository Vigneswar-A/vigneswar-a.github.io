class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        
        prereq = [[] for _ in range(n)]
        in_degree = [0] * n
        
        for pre,course in relations:
            prereq[pre-1].append(course)
            in_degree[course-1] += 1
            
        queue = deque(course for course,degree in enumerate(in_degree,1) if degree == 0)

        res = 0 if queue else -1
        while queue:
            for i in range(len(queue)):
                node = queue.popleft()
                for nxtnode in prereq[node-1]:
                    in_degree[nxtnode-1] -= 1
                    if in_degree[nxtnode-1] == 0:
                        queue.append(nxtnode)
            res += 1
            
        return res if not any(in_degree) else -1
                    
        
            
        