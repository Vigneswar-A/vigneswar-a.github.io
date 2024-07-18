class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        
        counts = Counter(letters)
        res = 0
        
        def backtrack(i=0, points=0):
            nonlocal res, counts
            if i == len(words):
                res = max(res, points)
                return 
            
            word_count = Counter(words[i])
            if counts > word_count:
                counts -= word_count
                backtrack(i+1, points+sum(score[ord(c)-ord('a')] for c in words[i]))
                counts += word_count
                
            backtrack(i+1, points)
            
        backtrack()
        
        return res
            
            