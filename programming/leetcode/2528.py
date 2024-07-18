class Solution:
    def countTime(self, time: str) -> int:
        
        res = 0
        for hr in range(24):
            for min in range(60):
                flag = True
                for test_digit, actual_digit in zip(time, f"{hr:0>2}:{min:0>2}"):
                    if test_digit == "?":
                        continue
                    elif test_digit != actual_digit:
                        flag = False
                        break
                res += flag
                
        return res
        