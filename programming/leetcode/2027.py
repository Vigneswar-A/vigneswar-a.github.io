class Solution:
    def maximumRemovals(self, s: str, p: str, removable: List[int]) -> int:
        def ispossible(k):
            nums = set(removable[:k])
            j = 0
            for i in range(len(s)):
                if i not in nums and s[i] == p[j]:
                    j += 1
                if j == len(p):
                    return False
            return True

        return bisect.bisect_left(range(1,len(removable)+1), 1, key=ispossible)

        