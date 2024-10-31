class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        res = []
        for word in queries:
            for target in dictionary:
                if len(word) == len(target) and sum(word[i] != target[i] for i in range(len(word))) <= 2:
                    res.append(word)
                    break
                    
                    
        return res
                    
                    
                    
                    
        



        