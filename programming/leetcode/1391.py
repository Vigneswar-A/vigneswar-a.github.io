class Solution:
    def countElements(self, arr: List[int]) -> int:
        arr.sort()
        res = 0
        count = 1
        for i in range(len(arr) - 1):
            if arr[i] == arr[i + 1]:
                count += 1
                continue
            if arr[i] + 1 == arr[i + 1]:
                res += count
            count = 1
                
        return res
                
        