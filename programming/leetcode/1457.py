class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        jobs = len(jobDifficulty)
        
        @cache
        def dp(job=0, day=0, max_job=0):
            
            if job == jobs and day == d:
                return max_job
            
            elif job == jobs:
                return float('inf')
            
            elif day == d:
                return dp(job+1, day, max(max_job, jobDifficulty[job]))
            
            return min(
                        dp(job+1, day, max(max_job, jobDifficulty[job])),
                        dp(job+1, day+1, jobDifficulty[job])+max_job
                    )
        
        return dp() if dp() != float('inf') else -1
            
        
            
        