class Solution:
    def minimizeResult(self, expression: str) -> str:
        n,_,m = map(len, expression.partition('+'))
        solved = ''
        res = inf
        for i in range(n):
            for j in range(1, m+1):
                if int(expression[:i] or '1')*eval(expression[i:n+j+1])*int(expression[n+j+1:] or '1') < res:
                    res = int(expression[:i] or '1')*eval(expression[i:n+j+1])*int(expression[n+j+1:] or '1')
                    solved = expression[:i]+'('+expression[i:n+j+1]+')'+expression[n+j+1:]

        return solved if eval(expression) > res else f'({expression})'
        