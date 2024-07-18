class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        
        counts = Counter(words)
        res = 0
        for word,count in counts.items():
            if word == word[::-1]:
                res += count//2
            else:
                res += min(count, counts[word[::-1]])
        return res//2
        
        