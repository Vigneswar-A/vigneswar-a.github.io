class Solution:
    def subarraysDivByK(self, nums, k):
        
        hashmap = Counter()
        total = 0
        count = 0

        for n in nums:
            total += n
            remainder = total%k
            
            if hashmap[remainder] > 0:
                count += hashmap[remainder]
                
            hashmap[remainder] += 1
            
        
                
        return count + hashmap[0]