class Solution:
    @lru_cache
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if not s3:
            return not (s1 or s2)
        if s1 and s1[0] == s3[0] and (not s2 or s2[0] != s3[0]):
            return self.isInterleave(s1[1:] , s2 , s3[1:])
        if s2 and s2[0] == s3[0] and (not s1 or s1[0] != s3[0]):
            return self.isInterleave(s1 , s2[1:] , s3[1:])
        if s1 and s2 and s1[0] == s2[0] == s3[0]:
            return self.isInterleave(s1[1:] , s2 , s3[1:]) or self.isInterleave(s1 , s2[1:] , s3[1:])
        return False
                
                
        
        