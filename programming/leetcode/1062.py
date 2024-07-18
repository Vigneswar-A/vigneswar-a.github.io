class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:

        prefix = list(accumulate(arr))

        count = 0
        if prefix[-1]%3:
            return False

        step = target = prefix[-1]//3
        count = 0
        for i in prefix:
            if i == target:
                count += 1
                target += step
                
        return count >= 3
