class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        return [comb for comb in combinations(range(1, 10) , k) if sum(comb) == n]
        