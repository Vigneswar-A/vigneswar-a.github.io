class Solution:
    def sumZero(self, n: int) -> List[int]:
        return tuple(itertools.chain.from_iterable((i,-i) for i in range(1,n//2+1)))+(0,)*(n%2)