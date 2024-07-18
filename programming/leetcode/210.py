class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        prereq = [[] for _ in range(numCourses)]
        in_degree = [0] * numCourses
        
        for course,pre in prerequisites:
            prereq[pre].append(course)
            in_degree[course] += 1
            
        queue = deque(course for course,degree in enumerate(in_degree) if degree == 0)
        
        res = []
        while queue:
            
            node = queue.popleft()
            res.append(node)
            
            for nxtnode in prereq[node]:
                in_degree[nxtnode] -= 1
                
                if in_degree[nxtnode] == 0:
                    queue.append(nxtnode)
     
        return res if len(res) == numCourses else []
            
        
            
            
        