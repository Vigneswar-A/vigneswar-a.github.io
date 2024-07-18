class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        n = len(arr)
        
        prefix = [inf]
        min_length = inf
        left = total = 0
        for right in range(n):
            total += arr[right]
            while total > target:
                total -= arr[left]
                left += 1
            if total == target:
                min_length = min(min_length, right-left+1)
            prefix.append(min_length)
            
        arr.reverse()
        suffix = []
        
        min_length = inf
        left = total = 0
        for right in range(n):
            total += arr[right]
            while total > target:
                total -= arr[left]
                left += 1
            if total == target:
                min_length = min(min_length, right-left+1)
            suffix.append(min_length)
        suffix.reverse()
        
        res = inf
        for l,r in zip(prefix, suffix):
            res = min(res, l+r)
            
        return res if res != inf else -1
            
         
        
           
            
            
        
        