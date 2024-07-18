class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        n=int(dividend/divisor)
        return (n if n<2147483648 else 2147483647)
        