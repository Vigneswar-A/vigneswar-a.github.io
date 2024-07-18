class Solution:
    def rearrangeString(self, s: str, k: int) -> str:
        from sortedcontainers import SortedDict
        counts = Counter(s)
        res = ''
        k = max(k, 1)
        flag = True
        while flag:
            flag = False
            i = 0
            for c in sorted(counts, key=counts.get, reverse=1):
                if i == k:
                    break
                if counts[c]:
                    flag = True
                    res += c
                    counts[c] -= 1
                    i += 1

        lastseen = defaultdict(lambda : -inf)
        for i,c in enumerate(res):
            if i-lastseen[c] < k:
                return ''
            lastseen[c] = i
            
        return res
                    
        