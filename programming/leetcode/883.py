class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        

        fleets = 0
        endtime = 0
        for pos,speed in sorted(zip(position, speed), reverse=1):
            currtime = (target-pos)/speed
            if currtime > endtime:
                fleets += 1
                endtime = currtime
                
        return fleets
                
                
        