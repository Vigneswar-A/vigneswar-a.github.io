class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        res = 0
        cont1 = 0
        cont2 = 0
        for i in range(len(arr)-1):
            if i%2:
                if arr[i] > arr[i+1]:
                    cont1 += 1
                    cont2 = 0
                elif arr[i] < arr[i+1]:
                    cont1 = 0
                    cont2 += 1
                else:
                    cont1 = cont2 = 0
            else:
                if arr[i] < arr[i+1]:
                    cont1 += 1
                    cont2 = 0
                elif arr[i] > arr[i+1]:
                    cont1 = 0
                    cont2 += 1
                else:
                    cont1 = cont2 = 0
            res = max(res, cont1, cont2)
        return res+1