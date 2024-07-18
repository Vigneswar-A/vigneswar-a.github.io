class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        
        worker.sort()
        ans = 0
        for profit,difficulty in sorted(zip(profit, difficulty), reverse=1):
            
            while True:
                
                idx = bisect.bisect_left(worker, 1, key = lambda d: d >= difficulty)
                if 0 <= idx < len(worker):
                    worker.pop(idx)
                    ans += profit
                else:
                    break
                
        return ans
            