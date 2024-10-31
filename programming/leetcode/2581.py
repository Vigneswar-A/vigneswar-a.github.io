class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        target = sum(skill)*2/len(skill)

        counts = Counter()
        res = 0
        
        for i in skill:
            if counts[target-i]:
                res += i*(target-i)
                counts[target-i] -= 1
            else:
                counts[i] += 1
                
        return int(res) if not any(counts.values()) else -1
                
        
        
        
        