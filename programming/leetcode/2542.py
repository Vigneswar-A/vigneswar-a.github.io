class Solution:
    def averageValue(self, nums: List[int]) -> int:
        
        divisible = [num for num in nums if num%6 == 0]
        return sum(divisible)//len(divisible) if divisible else 0
        