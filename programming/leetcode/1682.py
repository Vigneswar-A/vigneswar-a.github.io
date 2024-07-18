class Solution:
    def mostVisited(self, n: int, rounds: List[int]) -> List[int]:
        
        
        visiteds = Counter()
        visiteds[rounds[0]] = 1
        
        for i in range(len(rounds)-1):
            start, end = rounds[i], rounds[i+1]
            
            if start > end:
                end = n + end
                
            for track in range(start+1, end+1):
                if track > n:
                    track = track-n
                visiteds[track] += 1
            
        max_visits = max(visiteds.values())
        
        return sorted(track for track,count in visiteds.items() if count == max_visits)
            
        