# """
# This is GridMaster's API interface.
# You should not implement it, or speculate about its implementation
# """
#class GridMaster(object):
#    def canMove(self, direction: str) -> bool:
#        
#
#    def move(self, direction: str) -> int:
#        
#
#    def isTarget(self) -> None:
#        
#

class Solution(object):
    def findShortestPath(self, master: 'GridMaster') -> int:
        
        size = 201
        directions = {'U':(-1, 0), 'D':(1,0), 'L':(0,-1), 'R':(0,1)}
        opposites = {'U':'D', 'L':'R', 'R':'L', 'D':'U'}
        grid = [[inf]*size for _ in range(size)]
        si = sj = size//2
        ti = tj = None
        
        visited = set()
        
        def backtrack(i, j):
            nonlocal ti, tj
            if master.isTarget():
                ti = i
                tj = j
                
            for d,(dx,dy) in directions.items():
                if master.canMove(d) and (i+dx, j+dy) not in visited:
                    visited.add((i+dx, j+dy))
                    grid[i+dx][j+dy] = master.move(d)
                    backtrack(i+dx, j+dy)
                    master.move(opposites[d])
        
        backtrack(si, sj)
        
        if ti is None:
            return -1
        
        # dijkstra
        visited = set()
        heap = [(0, si, sj)]
        distance = [[inf]*size for _ in range(size)]
        distance[si][sj] = 0
        while heap:
            cost, i, j = heappop(heap)
            visited.add((i, j))
            for _,(dx,dy) in directions.items():
                adjcost = grid[i+dx][j+dy]
                if (i+dx, j+dy) not in visited and adjcost+cost < distance[i+dx][j+dy]:
                    distance[i+dx][j+dy] = cost+adjcost
                    heappush(heap, ((cost+adjcost, i+dx, j+dy)))

        
        return distance[ti][tj]
                    
                
                
                    
                
            
                    
                    
                    
                
            
                    