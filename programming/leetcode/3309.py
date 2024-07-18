class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        res = 0
        for i in range(len(words)):
            for j in range(i+1, len(words)):
                if str.startswith(words[j], words[i]) and str.endswith(words[j], words[i]):
                    res += 1
                    
        return res
                    
        