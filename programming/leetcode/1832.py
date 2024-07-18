class Solution:
    def minOperations(self, target: List[int], arr: List[int]) -> int:
        
        
        indices = {v:i for i,v in enumerate(target)}
        nums = []
        for i in arr:
            if i in indices:
                nums.append(indices[i])
                

        lis = []
        for i in nums:
            if not lis or i > lis[-1]:
                lis.append(i)
            else:
                j = bisect.bisect_left(lis, i)
                lis[j] = i

        return len(target) - len(lis)
            