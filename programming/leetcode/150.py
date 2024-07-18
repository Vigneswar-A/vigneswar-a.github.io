class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        operations = {"+":int.__add__, "-":int.__sub__, "*":int.__mul__, "/":lambda a,b : ceil(a/b) if a/b < 0 else floor(a/b)}
        stack = []
        for c in tokens:
            if c.isnumeric() or len(c) > 1:
                stack.append(int(c))
            else:
                op1 = stack.pop()
                op2 = stack.pop()
                print(op2, c, op1)
                stack.append(operations[c](op2, op1))
        
        return stack.pop()


                
                    