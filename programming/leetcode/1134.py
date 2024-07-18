class Solution:
    def shortestDistanceColor(self, colors: List[int], queries: List[List[int]]) -> List[int]:
        
        n = len(colors)
        left_prefix = [[0,0,0]] * n
        right_prefix = [[0,0,0]] * n
        
        prev_pos = [-float('inf')]*3
        next_pos = [float('inf')]*3
        
        for i in range(n):
            prev_pos[colors[i] - 1] = i
            left_prefix[i] = prev_pos[:]
            
            next_pos[colors[n-i-1]-1] = n-i-1
            right_prefix[n-i-2] = next_pos[:]

        right_prefix[-1] = [float('inf')] * 3
        
        res = []
        for idx,color in queries:
            left = left_prefix[idx][color-1]
            right = right_prefix[idx][color-1]
            
            temp = min(idx-left, right-idx)
            res.append(temp if temp != float('inf') else -1)
            
        return res
        
        
        