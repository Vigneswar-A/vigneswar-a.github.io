class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        
        heap = [(-profit,capital) for profit,capital in zip(profits, capital)]
        heapq.heapify(heap)
        
        cap = w
        
        while heap and k:
            temp = []
            while heap:
                profit, capital = heapq.heappop(heap)
                if capital <= cap:
                    k -= 1
                    cap -= profit
                    break
                temp.append((profit, capital))
            else:
                break
                
            for node in temp:
                heapq.heappush(heap, node) 
            
        return cap
        
        