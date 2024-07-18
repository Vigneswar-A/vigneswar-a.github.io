class Solution:
    def confusingNumberII(self, n: int) -> int:
        
        pairs = {'0':'0', '1':'1', '6':'9', '8':'8', '9':'6'}
        set_of_nums = {'0', '1', '6', '8', '9'}

        def backtrack(current = ''):

            if current and int(current) > n:
                return 0     

            return sum(backtrack(current + num) for num in set_of_nums) + (int(''.join(pairs[d] for d in current[::-1])) != int(current) if current != '' else 0)
        
        return sum(backtrack(num) for num in set_of_nums if num != '0')
        
        
        
        