class Solution:
    def generatePalindromes(self, s: str) -> List[str]:
        
        counts = Counter(s)
        evens = []
        center = ''
        
        for key,count in counts.items():
            if count%2:
                if center == '':
                    center = key
                    count -= 1
                else:
                    return []
            evens.extend(key*(count//2))
        
        res = []
        for perm in set(permutations(evens)):
            perm = ''.join(perm)
            res.append(perm + center + perm[::-1])
            
        return res
                
            
                
            
        