class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        
        size = len(s)
        def is_possible(n):
            cost = 0
            for i in range(n):
                cost += abs(ord(s[i]) - ord(t[i]))

            for i in range(size-n+1):
                if cost <= maxCost:
                    return True
                
                if i < size-n:
                    cost -= abs(ord(s[i]) - ord(t[i]))
                    cost += abs(ord(s[i+n]) - ord(t[i+n]))
                    
            return False

        return bisect.bisect_left(range(1, size+1), 1, key=lambda i: not is_possible(i))
                
        