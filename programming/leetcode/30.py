class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        size = len(''.join(words))
        length = len(words[0])
        
        def backtrack(initial):
            counts = Counter(words)
            for i in range(initial , initial + size, length):
                if counts[s[i:i+length]] > 0:
                    counts[s[i:i+length]] -= 1
                else:
                    return False
            return True
        
        res = []
        for i in range(len(s) - size + 1):
            if backtrack(i):
                res.append(i)
                
        return res
        
        