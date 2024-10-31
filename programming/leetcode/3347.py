class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        arr1 = []
        arr2 = []
        
        for i in nums:
            if not arr1 or (arr2 and arr1[-1] > arr2[-1]):
                arr1.append(i)
            else:
                arr2.append(i)
                
        return arr1+arr2
            
        