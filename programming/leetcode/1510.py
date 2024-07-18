class Solution:
    def findLucky(self, arr: List[int]) -> int:
        
        arr.sort(reverse = 1)
        
        prev = None
        count = 0
        for i in arr:
            if prev == i:
                count += 1
            else:
                if count == prev:
                    return prev
                prev = i
                count = 1
                
        return prev if prev == count else -1
            
        