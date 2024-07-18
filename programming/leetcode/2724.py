class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        
        counts = Counter(nums)
        res = []
        while counts:
            temp = []
            for i in counts:
                if counts[i]:
                    temp.append(i)
                    counts[i] -= 1
            if temp:
                res.append(temp)
            else:
                break
        return res
            
        