
class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        return functools.reduce(operator.xor,(start+(i<<1) for i in range(n)))