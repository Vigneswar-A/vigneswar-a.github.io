class Solution:
    def splitLoopedString(self, strs: List[str]) -> str:
        
        res  = ''
        for i in range(len(strs)):
            for j in range(len(strs[i])):
                s1 = strs[i][j:]
                s2 = strs[i][::-1][j:]     
                if s1+'~' < res and s2+'~' < res:
                    continue
                for k in range(i+1, len(strs)):
                    s1 += max(strs[k], strs[k][::-1])
                    s2 += max(strs[k], strs[k][::-1])
                for k in range(i):
                    s1 += max(strs[k], strs[k][::-1])
                    s2 += max(strs[k], strs[k][::-1])
                s1 += strs[i][:j]
                s2 += strs[i][::-1][:j]
                res = max(res, s1, s2)

        return res
        