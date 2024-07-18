class Solution:
    def totalMoney(self, n: int) -> int:
        
        day = 0
        money = 0
        prev_mon = 0
        prev_day = 0
        
        while day < n:
            if day%7 == 0:
                prev_mon += 1
                money += prev_mon
                prev_day = prev_mon
            else:
                prev_day += 1
                money += prev_day
                
            day += 1
            
        return money
        