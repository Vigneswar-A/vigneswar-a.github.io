class Solution:
    def splitIntoFibonacci(self, num: str) -> List[int]:

        res = []
        path = []
        n = len(num)
        max_val = 2**31

        def backtrack(curr = 0):
            nonlocal res
            if curr == n and len(path) > 2:
                res = path[:]
                return 

            if res:
                return 

            for next in range(curr, n):
                temp = num[curr : next+1]
                if len(temp) > 1 and temp[0] == '0':
                    continue
                currnum = int(temp)
                if len(path) < 2 or path[-1] + path[-2] == currnum and currnum < max_val:
                    path.append(currnum)
                    if backtrack(next+1):
                        break
                    path.pop()

        backtrack()
                    
        return res


                    

            
