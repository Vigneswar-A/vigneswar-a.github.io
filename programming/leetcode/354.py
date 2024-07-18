class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        
        envelopes.sort(key = lambda en: (en[0], -en[1]))
        n = len(envelopes)
        dp = [0]*n

        subseq = [envelopes[0][1]]
        for i in range(1, n):
            if subseq[-1] < envelopes[i][1]:
                subseq.append(envelopes[i][1])
            else:
                idx = bisect.bisect_left(subseq, envelopes[i][1])
                subseq[idx] = envelopes[i][1]
                
        return len(subseq)
            
        