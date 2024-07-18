class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        
        def get_primes(left, right):
            board = [True]*(right+1)
            board[1] = False
            
            for i in range(2, right+1):
                if board[i] is True:
                    for j in range(i*i, right+1, i):
                        board[j] = False
                        
            return [i for i in range(left, right+1) if board[i]]
        
        primes = get_primes(left, right)
        
        if len(primes) < 2:
            return -1,-1
        
        min_diff = inf
        for i in range(len(primes)-1):
            if primes[i+1]-primes[i] < min_diff:
                min_diff = primes[i+1]-primes[i]
                res = primes[i],primes[i+1]
                
        return res
            
                        
            
            
        