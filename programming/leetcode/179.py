class Solution:
    def largestNumber(self, nums: List[int]) -> str:
       
        
        class comp(str):
            def __lt__(self, other):
                
               
                if self.startswith(other) or other.startswith(self):
                    return int(self+other) < int(other+self)
                return str(self) < str(other)
        return str(int(''.join(sorted(map(comp, nums), reverse=True)) ))
        