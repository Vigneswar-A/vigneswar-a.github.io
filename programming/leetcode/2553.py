class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        
        heap = []
        
        for i in range(candidates):
            heappush(heap, (costs[i], i))
            if len(costs)-i-1 >= candidates:
                heappush(heap, (costs[-i-1], len(costs)-i-1))
            
        
        total_cost = 0
        
        left = candidates-1
        right = len(costs)-candidates
        while k:
            if right < left:
                break
            cost, i = heappop(heap)
            total_cost += cost
            
            
            if i <= left:
                left += 1
                if left < right:
                    heappush(heap, (costs[left], left))

                
            else:
                right -= 1
                if left < right:
                    heappush(heap, (costs[right], right))
                
            k -= 1
        
        if k:
            total_cost += sum(i for i,j in nsmallest(k, heap))
            
        return total_cost
        
            
        
        