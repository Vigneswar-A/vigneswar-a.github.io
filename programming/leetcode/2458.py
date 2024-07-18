class Solution:
    def minimumTime(self, jobs: List[int], workers: List[int]) -> int:
        
        jobs.sort()
        workers.sort()
        ans = 0
        for i in range(len(jobs)):
            ans = max(ans, ceil(jobs[i]/workers[i]))
            
        return ans
        