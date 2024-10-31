class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        
        nums.sort()
        
        def position(distance):
            left = 0
            pairs = 0
            for right in range(len(nums)):
                while (nums[right]-nums[left]) > distance:
                    left += 1
                pairs += (right-left)
            return pairs
        
        return bisect.bisect_left(range(max(nums)), k, key=position)
        
        
        
                
            