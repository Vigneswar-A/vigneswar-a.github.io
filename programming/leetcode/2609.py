class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        
        maxnum = max(nums)
        board = [True]*(maxnum + 1)
        board[1] = False
        
        for i in range(2, maxnum+1):
            if board[i] is True:
                for j in range(i*i, maxnum+1, i):
                    board[j] = False

        def get_factors(num):
            for i in range(1, int(num**0.5)+1):
                if num%i == 0:
                    if board[i]:
                        yield i
                    if board[num//i]:
                        yield num//i
        
                    
        seen = set(fact for num in nums for fact in get_factors(num))   
        return len(seen)
                
            
        