class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        
        
        counts = Counter(words)
        res = 0
        
        for word in counts.copy():
            if word == word[::-1]:
                temp = counts[word] - counts[word]%2
                res += temp*2
                counts[word] -= temp
            else:
                temp = min(counts[word], counts[word[::-1]])
                res += temp*4
                counts[word] -= temp
                counts[word[::-1]] -= temp
        return res + any(word == word[::-1] and counts[word] for word in counts)*2
        