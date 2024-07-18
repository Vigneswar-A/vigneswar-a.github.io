class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:

        res = []
        def backtrack(i=0, curr=''):
            if i == len(s):
                if curr.count('.') == 3 and all(int(ip) < 256 and str(int(ip)) == ip for ip in curr.split('.')):
                    res.append(curr)
                return

            if curr == '':
                backtrack(i+1, curr+s[i])
            elif curr[-1] != '.':
                backtrack(i+1, curr+s[i])
                backtrack(i+1, curr+'.'+s[i])

        backtrack()
        return res
            