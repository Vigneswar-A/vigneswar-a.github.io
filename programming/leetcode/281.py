class ZigzagIterator:
    def __init__(self, v1: List[int], v2: List[int]):
        x = min(len(v1), len(v2))
        self.arr = sum(zip(v1, v2), tuple())+tuple(v1[x:]) + tuple(v2[x:])
        self.i = -1
        

    def next(self) -> int:
        self.i += 1
        return self.arr[self.i]
        

    def hasNext(self) -> bool:
        return self.i < len(self.arr)-1
        

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())