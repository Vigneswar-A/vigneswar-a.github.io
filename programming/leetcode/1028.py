class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        
        res = []
        f = s = 0
        while f < len(firstList) and s < len(secondList):
            left, right = max(firstList[f][0], secondList[s][0]), min(firstList[f][1],secondList[s][1])
            if left <= right:
                res.append([left, right])
            if firstList[f][1] < secondList[s][1]:
                f += 1
            else:
                s += 1
                
        return res
