class Solution:
    def longestCommonSubsequence(self, arrays: List[List[int]]) -> List[int]:
        return [element for element in min(arrays,key=len) if all((element in array for array in arrays))]
