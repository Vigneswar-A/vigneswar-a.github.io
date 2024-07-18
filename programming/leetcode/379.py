class PhoneDirectory:

    def __init__(self, maxNumbers: int):
        self.book = [*range(maxNumbers)]

    def get(self) -> int:
        return self.book.pop(0) if self.book else -1
        

    def check(self, number: int) -> bool:
        return number in self.book
        

    def release(self, number: int) -> None:
        if not self.check(number):
            return self.book.insert(0 , number)
        


# Your PhoneDirectory object will be instantiated and called as such:
# obj = PhoneDirectory(maxNumbers)
# param_1 = obj.get()
# param_2 = obj.check(number)
# obj.release(number)