class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hashmap = {}

        for i,n in enumerate(nums):
            if i - hashmap.get(n , -sys.maxsize) <= k:
                return True
            hashmap[n] = i
            
        return False
        