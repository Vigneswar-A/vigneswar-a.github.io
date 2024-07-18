class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        nums = deque(range(len(s) + 1))
        res = []
        
        for c in s:
            if c == 'I':
                res.append(nums.popleft())
            else:
                res.append(nums.pop())
                
        return res + [nums[0]]
        