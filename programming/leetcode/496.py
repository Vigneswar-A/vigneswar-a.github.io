class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hashmap=dict((i,j) for j,i in enumerate(nums2))
        output=[-1]*(n:=len(nums1))
        
        for i in range(n):
            for j in nums2[hashmap[(current:=nums1[i])]:]:
                if j>current:output[i]=j;break;
        
        return output
        
                
        