class MyHashMap:

    def __init__(self):
        self.mappings = [None for _ in range(1000007)]

    def put(self, key: int, value: int) -> None:
        self.mappings[key] = value
        

    def get(self, key: int) -> int:
        return self.mappings[key] if self.mappings[key] != None else -1
        

    def remove(self, key: int) -> None:
        self.mappings[key] = None
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)