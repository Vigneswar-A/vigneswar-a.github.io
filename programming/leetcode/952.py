class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        
            
        sub = reduce(or_ , map(Counter , words2) , Counter())
        return [word for word in words1 if Counter(word) >= sub]
            
        
        