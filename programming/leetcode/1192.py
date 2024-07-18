class Solution:
    def maximizeSweetness(self, sweetness: List[int], k: int) -> int:
        
        def cut(x):
            sum = 0
            cuts = 0
            for s in sweetness:
                sum += s
                if sum >= x:
                    cuts += 1
                    sum = 0   
                    
                if cuts == k+1:
                    return True
                
            return False

        return bisect.bisect_left(range(1, 100000000000), 1, key=lambda i:not cut(i))
        