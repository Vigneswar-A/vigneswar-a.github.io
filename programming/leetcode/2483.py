class Solution:
    def taskSchedulerII(self, tasks: List[int], space: int) -> int:
        

        last_time = {}
        time = 0
        
        for task in tasks:
            if task not in last_time or last_time[task]+space < time: 
                time += 1
            else:
                postpone = space - (time - last_time[task]) + 1
                time += postpone
            last_time[task] = time

        return time
                