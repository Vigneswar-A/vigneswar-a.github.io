class Solution:
    def myAtoi(self, s: str) -> int:
        match = re.search(r'^[ ]*[+-]{0,1}\d+',s)
        ans = int(match.group() if match else 0)
        if ans > 2147483647:
            return 2147483647
        elif ans < -2147483648:
            return -2147483648
        else:
            return ans