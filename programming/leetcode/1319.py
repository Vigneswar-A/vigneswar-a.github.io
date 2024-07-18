from collections import Counter
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counts=[j for i,j in Counter(arr).most_common()]
        return len(counts)==len(set(counts))
        
        