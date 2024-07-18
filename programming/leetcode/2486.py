class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        counts = defaultdict(lambda: 0)
        flag = False
        for i in nums:
            if i%2:
                continue
            flag = True
            counts[i] += 1
            
        if not flag:
            return -1
            

        max_counts = 0
        for i,count in sorted(counts.items()):
            if count > counts[max_counts]:
                max_counts = i
                
        return max_counts
            
        