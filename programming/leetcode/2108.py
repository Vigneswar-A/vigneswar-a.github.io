class Solution:
    def minimizeTheDifference(self, mat: List[List[int]], target: int) -> int:
        
        sums = {0}
        for i in range(len(mat)):
            temp = set()
            limit = inf
            for j in range(len(mat[i])):
                for total in sums:
                    cand = total+mat[i][j]
                    if cand <= target:
                        temp.add(cand)
                    elif  cand > target and cand < limit:
                        limit = cand
                        temp.add(cand)
            sums = temp
            
        sums = sorted(sums)
        print(sums)
        if sums[-1] < target:
            return target-sums[-1]
        pos = bisect.bisect_left(sums, target)
        return min(abs(target-sums[pos-1]), abs(target-sums[pos]))
            
        
        