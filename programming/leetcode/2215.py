class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        c = Counter(digits)
        return sorted({i for i in range(100, 1000 , 2) if c >= Counter(map(int , str(i)))})
                
        