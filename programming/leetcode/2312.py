class Solution:
    def mostFrequent(self, nums: List[int], key: int) -> int:
        counts = defaultdict(lambda : 0)
        
        for i in range(len(nums) - 1):
            if nums[i] == key:
                counts[nums[i + 1]] += 1
                
        return max(counts , key = counts.get)
        