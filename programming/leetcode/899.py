class Solution:
    def binaryGap(self, n: int) -> int:
        pattern = re.compile(r'(?<=1)0*(?=1)')

       
   
        return max(*map(len, pattern.findall(bin(n))), -1, -1) + 1
        