class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        
        hashmap={0:-1}     
        count=0
        maxlen=0
        
        for i in range(len(nums)):
            
            count+=2*nums[i]-1
            
            if count in hashmap:
                maxlen=maxlen if maxlen>(temp:=i-hashmap[count]) else temp
                continue
            hashmap[count]=i

        return maxlen
