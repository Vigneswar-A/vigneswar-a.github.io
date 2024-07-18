class Solution:
    def kBigIndices(self, nums: List[int], k: int) -> int:
        from sortedcontainers import SortedList
        
        prefix = []
        ordered_list = SortedList()
        
        for i in nums:
            ordered_list.add(i)
            prefix.append(ordered_list.bisect_left(i))
            
        suffix = []
        ordered_list = SortedList()
        for i in nums[::-1]:
            ordered_list.add(i)
            suffix.append(ordered_list.bisect_left(i))
            
        return sum((u>=k and v>=k) for u,v in zip(prefix,reversed(suffix)))
    