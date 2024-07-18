class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        
        waiting = 0
        current_time = 0
        for arrival, time in customers:
            if arrival >= current_time:
                current_time = arrival+time
                waiting += time
            else:
                waiting += current_time-arrival+time
                current_time += time

        return waiting/len(customers)
        
                
        