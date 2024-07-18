from collections import Counter,deque
class Solution:
    def originalDigits(self, s: str) -> str:
        s=Counter(s)
        Numbers=deque()
        
        #zero
        Numbers.extend([0]*(t:=s['z']))
        s.subtract('zero'*t)
        
        #two
        Numbers.extend([2]*(t:=s['w']))
        s.subtract('two'*t)
        
        #four
        Numbers.extend([4]*(t:=s['u']))
        s.subtract('four'*t)
        
        #six
        Numbers.extend([6]*(t:=s['x']))
        s.subtract('six'*t)
        
        #nine
        Numbers.extend([8]*(t:=s['g']))
        s.subtract('eight'*t)
        
        #one
        Numbers.extend([1]*(t:=s['o']))
        s.subtract('one'*t)
        
        #three
        Numbers.extend([3]*(t:=s['h']))
        s.subtract('three'*t)
        
        #five
        Numbers.extend([5]*(t:=s['f']))
        s.subtract('five'*t)
        
        #seven
        Numbers.extend([7]*(t:=s['s']))
        s.subtract('seven'*t)
        
        #nine
        Numbers.extend([9]*s['i'])
        
        return ''.join(map(str,sorted(Numbers)))     