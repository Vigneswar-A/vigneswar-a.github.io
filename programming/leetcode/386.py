class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        yield from sorted(range(1,n+1) , key = str)
        