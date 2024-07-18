class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        res = []
        count = 0
        start = nums[0]
        for i in range(len(nums)-1):
            if nums[i]+1 == nums[i+1]:
                count += 1
                continue
            elif count:
                res.append(f"{start}->{start+count}")
                count = 0
            else:
                res.append(str(nums[i]))
            start = nums[i+1]
            
        if count:
            res.append(f"{start}->{start+count}")
        elif len(nums) > 1:
            res.append(str(nums[i+1]))
        elif len(nums) == 1:
            return [str(nums[0])]
            
            
        return res
                
                
        