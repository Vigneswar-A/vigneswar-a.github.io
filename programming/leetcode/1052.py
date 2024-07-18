class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> List[int]:
        
        def dist(worker_loc, bike_loc):
            return abs(worker_loc[0] - bike_loc[0]) + abs(worker_loc[1] - bike_loc[1])
        
        distances = []
        
        for i,worker in enumerate(workers):
            for j,bike in enumerate(bikes):
                distances.append((dist(worker, bike), i, j))
                
        distances.sort()
        assigned = [None]*len(workers)
        used_bikes = set()
        
        for d,w,b in distances:
            if assigned[w] is None and b not in used_bikes:
                assigned[w] = b
                used_bikes.add(b)
            
        return assigned
    
        