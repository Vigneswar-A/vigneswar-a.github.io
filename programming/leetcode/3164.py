class Solution:
    def lastVisitedIntegers(self, nums: List[int]) -> List[int]:
        
        seen = deque()
        ans = []
        k = 0
        
        for i in nums:
            if i > 0:
                seen.appendleft(i)
                k = 0
            else:
                if k < len(seen):
                    ans.append(seen[k])
                else:
                    ans.append(-1)
                k += 1
                    
        return ans
                