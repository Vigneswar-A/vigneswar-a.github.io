class Solution:
    def distinctNumbers(self, nums: List[int], k: int) -> List[int]:
        
        counts = Counter()
        for i in range(k):
            counts[nums[i]] += 1
        res = []
        for j in range(k, len(nums)):
            res.append(len(counts))
            
            counts[nums[j-k]] -= 1
            if counts[nums[j-k]] == 0:
                del counts[nums[j-k]]
            
            counts[nums[j]] += 1
            
        return res+[len(counts)]
            
        