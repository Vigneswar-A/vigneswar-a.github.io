class Solution:
    def catchMaximumAmountofPeople(self, team: List[int], dist: int) -> int:
        
        queue = deque()
        res = 0
        extras = deque()
        for i in range(len(team)):
            while queue and queue[0] < i-dist:
                queue.popleft()
                
            while extras and extras[0] < i-dist:
                extras.popleft()
                
            if team[i] == 0:
                if extras:
                    extras.popleft()
                    res += 1
                else:   
                    queue.append(i)
            else:
                if queue:
                    queue.popleft()
                    res += 1
                else:
                    extras.append(i)
                
        return res
                
            