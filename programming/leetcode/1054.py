class Solution:
    def bitwiseComplement(self, n: int) -> int:
        return int(''.join(map(lambda n:str(abs(int(n)-1)),bin(n)[2:])),2)