class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        
        res = []
        prev = None
        for word,group in zip(words, groups):
            if prev != group:
                prev = group
                res.append(word)
                
        return res
               

        
        