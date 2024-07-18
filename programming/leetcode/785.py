class Solution:
    def calculate(self, s: str) -> int:
        
        def priority(c):
            if c == '+' or c == '-':
                return 1
            elif c == '*' or c == '/':
                return 2
            
        def calculate(a, b, op):
            operations = {'+' : float.__add__, '-' : float .__sub__, '*' : float.__mul__}
            if op == '/':
                return  ceil(a/b) if (a > 0) ^ (b > 0) else a//b
            return operations[op](a, b)
            
        op = []
        nums = []
        for c in filter(None, re.split(r'([+-/*()])', s)):
            if c.isnumeric():
                nums.append(c)
            elif c != '(' and c != ')':
                while op and op[-1] != '(' and priority(op[-1]) >= priority(c):
                    a, b = nums.pop(), nums.pop()
                    nums.append(calculate(float(b), float(a), op.pop()))
                op.append(c)
            elif c == '(':
                op.append(c)
            else:
                while op and op[-1] != '(':
                    a, b = nums.pop(), nums.pop()
                    nums.append(calculate(float(b), float(a), op.pop()))
                op.pop()
                    
                    
        

        while op:
            a, b = nums.pop(), nums.pop()
            nums.append(calculate(float(b), float(a), op.pop()))

        return int(nums.pop())
            
        