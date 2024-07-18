class StringIterator:

    def __init__(self, compressedString: str):
        self.counts = deque()
        self.chars = deque()
        self.count = 0
        self.char = None
        
        temp = ''
        for c in compressedString:
            if c.isdigit():
                temp += c
            else:
                if temp:
                    self.counts.append(int(temp))
                    temp = ''
                self.chars.append(c)
        if temp:
            self.counts.append(int(temp))

    def next(self) -> str:
        if self.count == 0 and not self.counts:
            return ' '
        if self.count == 0:
            self.count = self.counts.popleft()
            self.char = self.chars.popleft()

        self.count -= 1
        return self.char
        

    def hasNext(self) -> bool:
        return (self.counts or self.count)
        


# Your StringIterator object will be instantiated and called as such:
# obj = StringIterator(compressedString)
# param_1 = obj.next()
# param_2 = obj.hasNext()