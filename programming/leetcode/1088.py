monthdays={1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
class Solution:
    def numberOfDays(self, year: int, month: int) -> int:
        return monthdays[month]+(month==2 and (year%400==0 or year%100 and year%4==0))
        
        