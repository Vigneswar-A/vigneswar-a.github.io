class Solution:
    def widestPairOfIndices(self, nums1: List[int], nums2: List[int]) -> int:
        
        diff = {0:-1}
        prefix1 = list(accumulate(nums1)) 
        prefix2 = list(accumulate(nums2)) 

        res = 0
        for i in range(len(prefix1)):
            if prefix1[i]-prefix2[i] in diff:
                res = max(res, i-diff[prefix1[i]-prefix2[i]])
            else:
                diff[prefix1[i]-prefix2[i]] = i
                
        return res
                
            
            
            
        
        
        