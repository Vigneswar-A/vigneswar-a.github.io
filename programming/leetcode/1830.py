class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        pows = [2 ** i for i in range(22)]
        freq = Counter()
        
        res = 0
        for num in deliciousness:
            for pw in pows:
                res += freq[pw - num]
            freq[num] += 1
                
        return res % (10**9 + 7)
                
                
                
        
        
        
                
                   
        