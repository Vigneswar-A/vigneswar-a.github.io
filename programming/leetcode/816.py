class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class MyHashSet:

    def __init__(self):
        self.map = [None] * 769

    def add(self, key: int) -> None:
        currnode = self.map[key%769]
        if currnode is None:
            self.map[key%769] = Node(key)
            return 
        
        while currnode.next:
            if currnode.val == key:
                return
            currnode = currnode.next
        
        if currnode.val == key:
            return
        
        currnode.next = Node(key)     
        
    def remove(self, key: int) -> None:
        currnode = self.map[key%769]
        if currnode is None:
            return
        
        if currnode.val == key:
            self.map[key%769] = currnode.next
            return
        
        while currnode.next:
            if currnode.next.val == key:
                currnode.next = currnode.next.next
                return 
            
            currnode = currnode.next

    def contains(self, key: int) -> bool:
        currnode = self.map[key%769]
        while currnode:
            if currnode.val == key:
                return True
            currnode = currnode.next
        return False
            
        
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)