from collections import Counter
class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        boxes=[]
        for n in range(lowLimit,highLimit+1):
            boxes.append(sum(map(int,str(n).strip())))
        return Counter(boxes).most_common(1)[0][1]
            
            
            
            
        