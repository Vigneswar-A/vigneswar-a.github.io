class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        def selfdividing(n):
            if '0' in str(n):return 0
            return not any(n%int(i) for i in str(n))
        return list(filter(selfdividing,range(left,right+1)))
            
            
        