from collections import deque
import re
class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        arr=[i for i in re.split(r'([a-z]|\d+)',abbr) if i!='']
        word=deque(word)
        for c in arr:
            if c.isdigit():
                if int(c)<=len(word) and c[0]!='0':
                    for _ in range(int(c)):
                        word.popleft()
                else:
                    return False
            elif c.isalpha():
                if len(word)!=0 and word[0]==c:
                    word.popleft()
                else:
                    return False
        return len(word)==0
        
        
         
            