class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:

        n = len(intervals)
        intervals.sort(key=lambda arr:(arr[-1], arr[0]))
        
        required = {i:2 for i in range(n)}
        nums = []
        for i in range(n):
            if required[i] == 2:
                nums.append(intervals[i][-1])
                nums.append(intervals[i][-1]-1)
                required[i] = 0
                for j in range(i+1, n):
                    if intervals[j][0] <= intervals[i][-1] <= intervals[j][-1]:
                        required[j] -= 1
                    if intervals[j][0] <= intervals[i][-1]-1 <= intervals[j][-1]:
                        required[j] -= 1
            elif required[i]== 1:
                if intervals[i][-1] not in nums:
                    nums.append(intervals[i][-1])
                else:
                    nums.append(intervals[i][-1]-1)
                required[i] = 0
                for j in range(i+1, n):
                    if intervals[j][0] <= nums[-1] <= intervals[j][-1]:
                        required[j] -= 1
                        
        return len(nums)
            
        