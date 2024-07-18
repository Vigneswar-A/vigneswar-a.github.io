class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.res = itertools.combinations(characters , combinationLength)
        self.Next = ''.join(next(self.res))
        

    def next(self) -> str:
        res = self.Next
        self.Next = ''.join(next(self.res , ''))
        return res
        
    def hasNext(self) -> bool:
        return self.Next
        


# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()