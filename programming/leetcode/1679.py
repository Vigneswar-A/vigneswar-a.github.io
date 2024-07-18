class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        if len(arr) == 1:
            return 0
        
        size = len(arr)
        res = float('inf')
        
        #remove right subarray
        for i in range(1, len(arr)):
            if arr[i-1] > arr[i]:
                break
        else:
            return 0
        
        left_wrong = i
        res = min(res, size-left_wrong)
        
        #remove left subarray
        for i in range(len(arr)-2,-1,-1):
            if arr[i+1] < arr[i]:
                break
        right_wrong = i
        res = min(res, right_wrong+1)
        
        for l in range(left_wrong):
            r = right_wrong+1
            while r < size and arr[r] < arr[l]:
                r += 1
            res = min(res, r-l-1)
        
        return res
        
        
        
                