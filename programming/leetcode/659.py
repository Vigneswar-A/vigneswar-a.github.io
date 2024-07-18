class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        
        counts = Counter(nums)
        res = []
        temp = []
        while counts:
            minval = min(counts)
            n = minval
            while counts[n] > 0:
                temp.append(n)
                counts[n] -= 1
                if counts[n] == 0:
                    del counts[n]
                n += 1
                
            res.append(temp)
            temp = []
            
        def check(i):
            if len(res[i]) >= 3:
                return True
            if i == 0:
                return False
            for j in range(i):
                if res[i][-1] + 1 in res[j]:
                    temp = res[j].index(res[i][-1] + 1)
                    res[i].extend(res[j][temp:])
                    del res[j][temp:]               
                    if check(j) and len(res[i]) >= 3:
                        return True
            
        for i in range(len(res)):
            if not check(i):
                return False

        return True
                
                
        