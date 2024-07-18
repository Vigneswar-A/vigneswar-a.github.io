class Solution:
    def longestBeautifulSubstring(self, word: str) -> int:
        
        
        left = right = res = 0
        n = len(word)
        while left < n and right < n:
            if word[right] != 'a':
                left = right = right+1
                continue
                
            for vowel in 'aeiou':
                flag = False
                while right < n and word[right] == vowel:
                    flag = True
                    right += 1

                if not flag:
                    break
            else:
                res = max(res, right-left)

            left = right
            
        return res
                
            