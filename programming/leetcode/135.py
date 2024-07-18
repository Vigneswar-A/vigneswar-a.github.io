class Solution:
    def candy(self, ratings: List[int]) -> int:
        indices = sorted(range(len(ratings)), key=ratings.__getitem__)
        res = [0]*len(ratings)

        for i in indices:
            if i-1 >= 0 and ratings[i] > ratings[i-1]: 
                res[i] = max(res[i-1]+1, res[i])
            if i+1 < len(ratings) and ratings[i] > ratings[i+1]:
                res[i] = max(res[i+1]+1, res[i])
            res[i] = max(res[i], 1)
            
        return sum(res)
            
        