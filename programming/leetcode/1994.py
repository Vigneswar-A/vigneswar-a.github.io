class Solution:
    def minSwaps(self, s: str) -> int:
        get_next = cycle(['0', '1'])
        swap1 = 0
        swap2 = 0
        zero_count = 0
        one_count = 0
        
        for c in s:
            current = next(get_next)
            if c == '0':
                zero_count += 1
            else:
                one_count += 1
                
            if current != c:
                swap1 += 0.5
            else:
                swap2 += 0.5
             
        
        if abs(zero_count-one_count) > 1:
            return -1
        elif zero_count > one_count:
            return int(swap1)
        elif one_count > zero_count:
            return int(swap2)
        else:
            return min(int(swap1), int(swap2))
                