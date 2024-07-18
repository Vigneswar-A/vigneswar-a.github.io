class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key = lambda arr : (arr[1] , arr[0]))
        res = 0
        
        while truckSize > 0 and boxTypes:
            n , unit = boxTypes.pop()
            box = min(truckSize , n)
            truckSize -= box
            res += unit * box
            
        return res
        