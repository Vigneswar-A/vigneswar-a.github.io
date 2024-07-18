class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        
        if k > len(arr):
            return max(arr)
        
        queue = deque(arr)
        score = Counter()
        
        while True:
            if queue[0] > queue[1]:
                score[queue[0]] += 1
                
                if score[queue[0]] == k:
                    return queue[0]
                winner = queue.popleft()
                queue.append(queue.popleft())
                queue.appendleft(winner)
                
                
            else:
                score[queue[1]] += 1
                if score[queue[1]] == k:
                    return queue[1]
                queue.append(queue.popleft())
                