class Solution:
    def findLonelyPixel(self, picture: List[List[str]]) -> int:
        m,n = len(picture),len(picture[0])
        
        rows = Counter()
        cols = Counter()

            
        for i in range(m):
            for j in range(n):
                if picture[i][j] == "B":
                    rows[i] += 1
                    cols[j] += 1

        count = 0
        for i in range(m):
            for j in range(n):
                if picture[i][j] == "B" and rows[i] == cols[j] == 1:
                    count += 1
                   
        return count
                    
            