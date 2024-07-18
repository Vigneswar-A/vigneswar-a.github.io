class Solution:
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
        
        arr2.sort()
        
        @cache
        def dp(i, prev):
            if i == len(arr1):
                return 0
            
            ans = inf
            if arr1[i] > prev:
                ans = dp(i+1, arr1[i])
                
            j = bisect.bisect(arr2, prev)
            if j < len(arr2) and arr2[j] > prev:
                ans = min(ans, dp(i+1, arr2[j])+1)
                    
            return ans
        
        ans = dp(0, -inf)
        return ans if ans != inf else -1
                
                
        