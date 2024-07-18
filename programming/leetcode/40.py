class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        candidates.sort()
        
        @cache
        def backtrack(start=0, path=tuple(), sums=0):
            if sums == target:
                yield path
            elif sums > target:
                return None
                
            for i in range(start, n):
                yield from backtrack(i+1, path+(candidates[i],), sums+candidates[i])           
        
        res = set(backtrack())
        return res
            
        