class Solution:
    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:
        
        res = []
        
        for i in range(n := len(favoriteCompanies)):
            for j in range(n):
                if i == j:
                    continue
                
                if set(favoriteCompanies[i]) < set(favoriteCompanies[j]):
                    break
            else:
                res.append(i)
                
        return res