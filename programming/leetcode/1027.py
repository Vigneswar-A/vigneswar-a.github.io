class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        
        currsum = sum(i for i in nums if i%2 == 0)
        res = []
    
        for val, idx in queries:
            prev = nums[idx]
            nums[idx] += val
            
            if nums[idx]%2 and prev%2 == 0:
                currsum -= prev
            elif prev%2 and nums[idx]%2 == 0:
                currsum += nums[idx]
            elif prev%2==0 and nums[idx]%2 == 0:
                currsum += val
                
            res.append(currsum)
            
        return res
        