class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        l,r=0,len(colors)-1
        lmax=rmax=0
        
        while l<r:
            if colors[l]!=colors[r]:
                lmax=r-l
                break
            l+=1
            
        l,r=0,len(colors)-1
        
        while l<r:
            if colors[l]!=colors[r]:
                rmax=r-l
                break
            r-=1 
        return max(lmax,rmax)
        
            
            
            
            
            
            
        