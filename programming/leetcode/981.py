class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        
        count = 0
        for i in range(len(strs[0])):
            prev = ''
            for s in strs:
                if not prev:
                    prev = s[i]
                    continue
                if s[i] < prev:
                    count += 1
                    break
                prev = s[i]

        return count
    
        
    
        