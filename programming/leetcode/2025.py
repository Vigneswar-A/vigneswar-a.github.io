class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        
        n = len(words)
        return all(i%n == 0 for i in Counter(''.join(words)).values())