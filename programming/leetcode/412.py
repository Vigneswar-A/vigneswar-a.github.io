class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        res = [''] * n
        hashset = {3 : "Fizz" , 5 : 'Buzz'}
        for i in range(1 , n + 1):
            if i % 3 == 0:
                res[i - 1] += hashset[3]
            if i % 5 == 0:
                res[i - 1] += hashset[5]
            if not res[i - 1]:
                res[i - 1] += str(i)
                
        return res
        