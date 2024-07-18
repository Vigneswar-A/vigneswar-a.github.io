class Solution:
    def gridIllumination(self, n: int, lamps: List[List[int]], queries: List[List[int]]) -> List[int]:
        rows = Counter()
        cols = Counter()
        diags = Counter()
        adiags = Counter()
        grid = Counter()
        
        def get_diag(i, j):
            return i+j
        
        def get_adiag(i, j):
            return i-j
        
        for i,j in lamps:
            if grid[(i,j)] == 0:
                rows[i] += 1
                cols[j] += 1
                diags[get_diag(i, j)] += 1
                adiags[get_adiag(i, j)] += 1
            grid[(i,j)] = 1
            
        res = []
        for i,j in queries:
            res.append(int(bool(rows[i] or cols[j] or diags[get_diag(i, j)] or adiags[get_adiag(i, j)])))
            for dx,dy in [(0,1),(1,0),(-1,0),(0,-1),(1,1),(-1,-1),(-1,1),(1,-1),(0,0)]:
                if 0 <= i+dx < n and 0 <= j+dy < n:
                    if grid[(i+dx, j+dy)]:
                        grid[(i+dx,j+dy)] = 0
                        rows[i+dx] -= 1
                        cols[j+dy] -= 1
                        diags[get_diag((i+dx), (j+dy))] -= 1
                        adiags[get_adiag((i+dx), (j+dy))] -= 1
                        
        return res


            
        