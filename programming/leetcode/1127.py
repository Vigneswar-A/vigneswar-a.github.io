class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        while len(stones)>1:
            currmax=0
            maxindex=0
            for i,n in enumerate(stones):
                if n>currmax:
                    currmax=n
                    maxindex=i
            
            stones.pop(maxindex)
            deleted=currmax
            
            currmax=0
            for i,n in enumerate(stones):
                if n>currmax:
                    currmax=n
                    maxindex=i
            
            stones.pop(maxindex)
            
            if currmax!=deleted:
                stones.append(deleted-currmax) 
        
        return 0 if not stones else stones[0]
                
        
        