class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        
        def get_maxdiff(arr):
            arr.sort()
            max_diff = 0
            for i in range(len(arr) - 1):
                if (diff := arr[i + 1] - arr[i]) > max_diff:
                    max_diff = diff
            return max_diff
        
        return get_maxdiff([0, *horizontalCuts, h]) * get_maxdiff([0, *verticalCuts, w])%1000000007
                
            