class Solution:
    def minimumSubstringsInPartition(self, s: str) -> int:
        
        @cache
        def dp(i=0):
            if i == len(s):
                return 0
            res = inf
            counts = Counter()
            counts_of_counts = Counter()
            for j in range(i, len(s)):
                if counts_of_counts[counts[s[j]]]:
                    counts_of_counts[counts[s[j]]] -= 1
                if counts_of_counts[counts[s[j]]] == 0:
                    del counts_of_counts[counts[s[j]]]
                counts[s[j]] += 1
                counts_of_counts[counts[s[j]]] += 1
                if len(counts_of_counts) == 1:
                    res = min(res, dp(j+1)+1)
            return res
        
        return dp()
                       
                    
                
        