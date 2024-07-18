class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
         
        pairs.sort()
        count = 1
        prev = pairs[0]
        for pair in pairs:
            if prev[1] < pair[0]:
                count += 1
            elif pair[-1] >= prev[1]:
                continue
            prev = pair

        return count
                
            
        
        
        