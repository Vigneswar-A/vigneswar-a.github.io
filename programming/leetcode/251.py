class Vector2D:

    def __init__(self, vec: List[List[int]]):
        self.list = iter(sum(vec , []))
        

    def next(self) -> int:
        return next(self.list)
        

    def hasNext(self) -> bool:
        dup = copy.copy(self.list)
        return next(dup , False) is not False
        


# Your Vector2D object will be instantiated and called as such:
# obj = Vector2D(vec)
# param_1 = obj.next()
# param_2 = obj.hasNext()