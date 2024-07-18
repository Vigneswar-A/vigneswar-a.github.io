class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        
        
        queue = deque(students)
        sandwiches.reverse()
        count = 0
        
        while queue:
            if count == len(queue):
                return len(queue)
            
            if sandwiches[-1] == queue[0]:
                count = 0
                queue.popleft()
                sandwiches.pop()
            
            else:
                queue.append(queue.popleft())
                count += 1
                
        return 0
            
            
                
            
        