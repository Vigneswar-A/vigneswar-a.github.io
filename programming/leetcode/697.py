class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        degree = (counts := Counter(nums)).most_common(1)[0][1]
        possibles = {i for i,j in counts.items() if j == degree}
        shortest = float('inf')
        rev = nums[::-1]
        n = len(nums)
        for num in possibles:
            shortest = min(shortest , n - rev.index(num) - nums.index(num))
        
        return shortest
        
        
        