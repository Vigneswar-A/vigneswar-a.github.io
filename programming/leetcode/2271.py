class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        
        positive = []
        negative = []
        
        for i in nums:
            (negative if i < 0 else positive).append(i)
            
        res = []
        for i in range(len(positive)):
            res.append(positive[i])
            res.append(negative[i])
            
        return res
    

        