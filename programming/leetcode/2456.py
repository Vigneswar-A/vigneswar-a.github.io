class Solution:
    def smallestNumber(self, pattern: str) -> str:
        
        nums = set(range(1, 10))
        ans = None
        res = []
        def backtrack(i=-1):
            nonlocal ans
            
            if i == len(pattern):
                
                ans = min(ans, ''.join(map(str, res))) if ans else ''.join(map(str, res))
                return
                
            for num in set(nums):
                if not res or pattern[i] == 'I' and num > res[-1] or pattern[i] == 'D' and num < res[-1]:
                    res.append(num)
                    nums.remove(num)
                    backtrack(i+1)
                    
                    nums.add(res.pop())
        backtrack()
        return ans
              
                    
                    
                
                    
                    
                
            
        