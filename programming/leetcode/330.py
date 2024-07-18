class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        included = 0
        i = 0
        patches = 0
        nums.append(inf)
        while included < n:
            if nums[i] > included+1:
                included = included*2+1
                patches += 1
            else:
                included += nums[i]
                i += 1
                
                
        return patches