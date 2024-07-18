class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if s == goal:
            return any(s.count(i) > 1 for i in s)
        
        x = y = 0
        for i in range(len(s)):
            if s[i] != goal[i]:
                x = i
                break
                
        for i in range(i + 1 , len(s)):
            if s[i] != goal[i]:
                y = i
                break
            
        s = list(s)
        
        s[x] , s[y] = s[y] , s[x]

        return s == list(goal)