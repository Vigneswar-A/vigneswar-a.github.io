class Solution:
    def nearestPalindromic(self, n: str) -> str:
        s = list(map(int, n))
        m = len(s)
        def calculate(s):
            try:
                temp = s
                for i in range(len(temp)):
                    if temp[i] != temp[-i-1]:
                        temp[-i-1] = temp[i]
                return str(int(''.join(map(str, temp))))
            except:
                return '10000'
                
        #case 1 (same middle)
        res1 = calculate(s)
        
        # case 2 (increment middle)
        s[m//2] += 1
        if m%2 == 0:
            s[m//2-1] += 1
        res2 = calculate(s)
    
        # case 3 (decrement mmiddle)
        if s[m//2] == 1:
            s[m//2] = 9
            if m%2 == 0:
                s[m//2-1] -= 2
            s[m//2-1] = 9 
            s[m//2-2] -= 1
            res3 = calculate(s)
            s[m//2-2] += 1
        else:
            s[m//2] -= 2
            if m%2 == 0:
                s[m//2-1] -= 2
            res3 = calculate(s)

        
        res4 = calculate(list(str(10**(m-1) - 1)))
        
        res5 = calculate(list(str(10**(m) + 1)))
        
        return min(res1, res2, res3, res4, res5, key=lambda c:(abs(int(n)-int(c)) if int(n) != int(c) and c == c[::-1] else inf, int(c)))