class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        return sorted(list(range(n:=len(mat))),key=lambda row:mat[row].count(1))[:k]
        