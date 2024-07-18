class Solution:
    def findInteger(self, k: int, digit1: int, digit2: int) -> int:
        
        heap = [0]
        visited = set()
        
        while heap:
            num = heappop(heap)
            if num > 2**31 - 1:
                break
            if num in visited:
                continue
            visited.add(num)
            if num%k == 0 and num > k:
                return num
            
            heappush(heap, num*10+digit1)
            heappush(heap, num*10+digit2)
            
        return -1