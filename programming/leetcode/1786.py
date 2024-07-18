class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed=set(allowed)
        return sum(word<=allowed for word in map(set,words))
            
        