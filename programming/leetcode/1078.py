class Solution:
    def removeOuterParentheses(self, s: str) -> str:

        res = ""
        temp = ""
        count = 0

        for c in s:
            if c == "(":
                count += 1
            else:
                count -= 1
            temp += c
            if count == 0:
                res += temp[1:-1]
                temp = ""
                
        return res
