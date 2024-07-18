class Solution:
    def minimumOperations(self, num: str) -> int:
        if num == '0':
            return 0
        if len(num) == 1 or (len(num) == 2 and num[1] == '0' and num[0] != '5'): return 1
        num = list(num)
        def get_cost(dig1, dig2, num):
            res = 0
            while num and num[-1] not in dig1:
                num.pop()
                res += 1
                
            if not num:
                return res
            num.pop()
            
            while num and num[-1] not in dig2:
                num.pop()
                res += 1

            return (res if num else res+1)
        
        ans = min(get_cost('5', '27', num[:]), get_cost('0', '50', num[:]))
        if ans == len(num):
            return ans-num.count('0')
        return ans