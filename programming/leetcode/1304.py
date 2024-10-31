class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        
        heap = [(-a, 'a'), (-b, 'b'), (-c, 'c')]
        heapify(heap)
        res = ''
        while heap:
            count, char = heappop(heap)
            if not count:
                continue
            if len(res) >= 2 and res[-1] == res[-2] == char:
                count2, char2 = heappop(heap)
                if not count2:
                    break
                res += char2
                heappush(heap, (count2+1, char2))
                heappush(heap, (count, char))
            else:
                res += char
                heappush(heap, (count+1, char))
        return res
            
        