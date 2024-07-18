class Solution:
    def timeTaken(self, arrival: List[int], state: List[int]) -> List[int]:
        
        n, time, prevstate, i = len(arrival), 0, 1, 0
        enterq = deque()
        exitq = deque()
        res = [0]*len(arrival)

        while i < n or enterq or exitq:
            while i < n and arrival[i] <= time:
                (exitq if state[i] else enterq).append(i)
                i += 1
                
            if (prevstate == 0 or not exitq) and enterq:
                res[enterq.popleft()] = time
                prevstate = 0
            elif exitq:
                res[exitq.popleft()] = time
                prevstate = 1
            else:
                prevstate = 1
                    
            time += 1
            
        return res

            
            