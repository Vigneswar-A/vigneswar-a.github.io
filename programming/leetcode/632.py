class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        k = len(nums)
        arr = sorted((num,i)  for i,sub in enumerate(nums) for num in sub)
        counts = Counter()
        distinct = right = 0
        lans, rans = -inf, inf
    
        for left in range(len(arr)):
            while distinct < k and right < len(arr):
                if not counts[arr[right][1]]:
                    distinct += 1
                counts[arr[right][1]] += 1         
                right += 1
            if distinct == k and right-1 < len(arr) and arr[right-1][0]-arr[left][0] < rans-lans:
                rans = arr[right-1][0]
                lans = arr[left][0]
            counts[arr[left][1]] -= 1
            if not counts[arr[left][1]]:
                distinct -= 1
        return [lans, rans]
                
            
        
            
            
        