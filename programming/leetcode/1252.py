class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        
        n = len(palindrome)
        if n == 1:
            return ""
        as_list = list(palindrome)
        
        if as_list[0] == "a":
            i = 0
            while i < n and as_list[i] == 'a':
                i += 1
                
            if i < n//2:
                as_list[i] = "a"
            else:
                as_list[-1] = "b"
        else:
            as_list[0] = "a"
                
                
        return "".join(as_list)
        