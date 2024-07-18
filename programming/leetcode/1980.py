class Solution:
    def badSensor(self, sensor1: List[int], sensor2: List[int]) -> int:
        
        for i in range(size:=len(sensor1)):
            if sensor1[i]!=sensor2[i]:
                break
                
        for i in range(i+1,size):            
            if sensor1[i]!=sensor2[i-1]:return 1
            if sensor2[i]!=sensor1[i-1]:return 2
        
            
        return -1
                
        
                
        
        