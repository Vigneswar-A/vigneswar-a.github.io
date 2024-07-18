class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        
        value = {c:i for i,c in enumerate(order)}
        
        return sorted(words, key=lambda word : tuple(value[c] for c in word)) == words
        