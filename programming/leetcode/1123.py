class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        
        hashmap=dict(map(reversed,enumerate(keyboard)))
        
        distance,currentpos=0,0
        
        for i in word:
            distance+=abs(currentpos-(currentpos:=hashmap[i]))
            
        return distance
            
            
            
        