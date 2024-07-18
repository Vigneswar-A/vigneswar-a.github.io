class Solution:
    def modifyString(self, s: str) -> str:
        s = list(s)
        size = len(s) - 1
        if not size:
            return s if s[0] != '?' else 'a'
        for i in range(len(s)):
            if s[i] == '?':
                for c in string.ascii_lowercase:
                    if i == 0 and s[i + 1] != c:
                        s[i] = c
                    elif i == size and s[i - 1] != c:
                        s[i] = c
                    elif 0 < i < size and s[i - 1] != c != s[i + 1]:
                        s[i] = c
                    
        return ''.join(s)
                
        