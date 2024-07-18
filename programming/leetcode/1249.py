class SnapshotArray:

    def __init__(self, length: int):
        self.id = 0
        self.changes = [[[-1, 0]] for _ in range(length)]
        

    def set(self, index: int, val: int) -> None:
        self.changes[index].append([self.id, val])

    def snap(self) -> int:
        self.id += 1
        return self.id-1
        

    def get(self, index: int, snap_id: int) -> int:
        i = bisect.bisect(self.changes[index], [snap_id + 1]) - 1
        return self.changes[index][i][1]

