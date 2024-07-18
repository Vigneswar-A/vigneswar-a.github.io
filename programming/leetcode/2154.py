class Solution:
    def minimumMoves(self, s: str) -> int:
        res = 0
        if 'XXX' in s:
            res += s.count('XXX')
            s = s.replace('XXX', '')
            
        if 'XXO' in s:
            res += s.count('XXO')
            s = s.replace('XXO', '')
            
        if 'OXX' in s:
            res += s.count('OXX')
            s = s.replace('OXX', '')
        
        if 'XOX' in s:
            res += s.count('XOX')
            s = s.replace('XOX', '')     
            
        if 'XX' in s:
            res += s.count('XX')
            s = s.replace('XX', '')
            
        return res + s.count('X')
            
            
            
        