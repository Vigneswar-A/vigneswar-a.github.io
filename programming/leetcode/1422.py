class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        
        count = Counter(nums)
        
        while count:
            num = min(count)
            for i in range(k):
                if count[num+i] < 1:
                    return False
                count[num+i] -= 1
                if count[num+i] == 0:
                    del count[num+i]
        
        return True
        