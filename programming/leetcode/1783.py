class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        
        prefix = []
        even = odd = 0
        for i in range(len(nums)):
            if i%2:
                odd += nums[i]
            else:
                even += nums[i]
            prefix.append((odd, even))
            
        prefix.append((0, 0))
        count = 0
        for i in range(len(nums)):
            u,v = prefix[-2]
            x,y = prefix[i]
            n,m = prefix[i-1]
            if (v-y+n) == (u-x+m):
                count += 1
        return count
            
            
            
                
            
        
        