class Solution:
    def maximumBeauty(self, flowers: List[int]) -> int:
        
        n = len(flowers)
        hashmap = {}
        for i in range(n-1,-1,-1):
            if flowers[i] not in hashmap:
                hashmap[flowers[i]] = i
        
        
        prefix = [0]*(n+1)
        
        for i in range(n):
            
            prefix[i] += prefix[i-1] + max(0,flowers[i])
            
        ans = -inf
        for i in range(n):
            if hashmap[flowers[i]] != i:
                ans = max(ans, prefix[hashmap[flowers[i]]-1] - prefix[i] + flowers[i]*2)
                
        return ans
            
         

                
        
        
        
        
        
        
        