dp={0:0,1:1,2:1}
class Solution:
    def countBits(self, n: int) -> List[int]:
        array=[]
        for i in range(n+1):
            
            if i in dp:
                array.append(dp[i])
                continue
            
            temp=i.bit_count()           
            array.append(temp)           
            dp[i]=temp
            
        return array
        