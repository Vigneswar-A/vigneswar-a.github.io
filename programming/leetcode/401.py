class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        
        ans = []
        for hr in range(12):
            for min in range(60):                    
                if hr.bit_count() + min.bit_count() == turnedOn:
                    ans.append(f"{hr:}:{min:0>2}")
                    
        return ans
                    
                