class FileSharing:

    def __init__(self, m: int):
        from sortedcontainers import SortedList
        self.chunks = defaultdict(set)
        self.users = SortedList(range(1, m+1))
        self.userchunk = defaultdict(list)


    def join(self, ownedChunks: List[int]) -> int:
        id = self.users[0]
        self.users.remove(id)
        for chunk in ownedChunks:
            self.chunks[chunk].add(id)
        self.userchunk[id] = ownedChunks
        return id
    
    def leave(self, userID: int) -> None:
        for chunk in self.userchunk[userID]:
            self.chunks[chunk].remove(userID)
        self.users.add(userID)
        self.userchunk[userID] = None
        

    def request(self, userID: int, chunkID: int) -> List[int]:
        res = sorted(self.chunks[chunkID])
        if res and userID not in res:
            self.userchunk[userID].append(chunkID)
            self.chunks[chunkID].add(userID)
        return res
        
        


# Your FileSharing object will be instantiated and called as such:
# obj = FileSharing(m)
# param_1 = obj.join(ownedChunks)
# obj.leave(userID)
# param_3 = obj.request(userID,chunkID)