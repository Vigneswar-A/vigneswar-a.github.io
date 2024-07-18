class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:

        queue = [*rooms[0]]
        visited = [0] * len(rooms)
        visited[0] = True

        while queue:
            node = queue.pop()

            for adj in rooms[node]:
                if not visited[adj]:
                    queue.append(adj)
                        
            visited[node] = True

        return all(visited)