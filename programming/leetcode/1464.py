class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        end = len(arr)//2
        count = 0
        for k,v in Counter(arr).most_common():
            end -= v
            count += 1
            if end <= 0:
                return count
            
        return None
                
                    
        