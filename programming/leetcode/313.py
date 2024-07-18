class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        count = 0
        heap = [1] 
        heapq.heapify(heap)
        
        prev = 0
        while count < n: 
            node = heapq.heappop(heap)
            if prev == node:
                continue
            prev = node
            count += 1
            for prime in primes:
                heapq.heappush(heap , node*prime)
                
        return node
                
        