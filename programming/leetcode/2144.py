class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        res = -1
        stack = []

        for num in nums:
            if stack and num < stack[-1]:
                res = max(res, stack[-1]-stack[0])
                while stack and num < stack[-1]:
                    stack.pop()
            stack.append(num)

        return max(res, stack[-1]-stack[0]) or -1

