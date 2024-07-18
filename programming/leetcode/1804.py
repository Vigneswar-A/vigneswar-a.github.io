class Solution:
    def maximumBinaryString(self, binary: str) -> str:
        n = len(binary)
        res = ['1']*n
        if '0' in binary:
            res[binary.count('0')-1+binary.index('0')] = '0'
        return ''.join(res)
            
        