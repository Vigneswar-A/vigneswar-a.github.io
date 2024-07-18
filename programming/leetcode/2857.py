class Solution:
    def distanceTraveled(self, mainTank: int, additionalTank: int) -> int:
        
        
        dist = 0
        while mainTank >= 5:
            mainTank -= 5
            dist += 50
            if additionalTank:
                additionalTank -= 1
                mainTank += 1
            
        return dist + mainTank*10
                
        