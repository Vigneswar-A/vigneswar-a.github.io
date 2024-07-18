class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        return sum(([i]*j for i,j in functools.reduce(operator.__and__,map(collections.Counter,words)).items()),[])
        