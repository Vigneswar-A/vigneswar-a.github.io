class Solution:
    def smallestString(self, s: str) -> str:
        temp = ''
        for c in s:
            if c == 'a':
                temp += 'a'
            else:
                break
        s = s[len(temp):]
        if 'a' in s:
            first, last = s.split('a', 1)
            last = 'a'+last
        else:
            first = s
            last = ''
        
        if set(temp+s) == {'a'}:
            return temp[:-1]+'z'
        
            
           
        
        return temp+''.join(chr(((ord(c)-ord('a'))-1)%26+ord('a')) for c in first)+last
        