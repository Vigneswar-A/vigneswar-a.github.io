class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        return [i for i,j in collections.Counter(s[i: i+10] for i in range(len(s) - 9)).items() if j > 1]
            
        