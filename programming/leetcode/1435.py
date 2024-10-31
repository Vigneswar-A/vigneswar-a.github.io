class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        bit_prefix = list(accumulate(arr, int.__xor__)) + [0]
                
        res = []
        for u,v in queries:
            res.append(bit_prefix[u-1]^bit_prefix[v])
        return res
                
            