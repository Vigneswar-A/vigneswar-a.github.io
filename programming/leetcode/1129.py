class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        
        words = set(words)
        
        @cache
        def backtrack(word , count=0):
            if word == '' or word not in words:
                return count
    
            return max(backtrack(word[:i] + word[i+1:] , count+1) for i in range(len(word)))
        
        return max(map(backtrack , words))