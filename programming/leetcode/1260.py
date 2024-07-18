monthdays=(0,0,31,59,90,120,151,181,212,243,273,304,334)
class Solution:
    def dayOfYear(self, date: str) -> int:
        
        year,month,day=map(int,date.split('-'))
        
        def isleap(year):
            return (year%400==0 or year%4==0 and year%100 )and month>2

        return monthdays[month]+ isleap(year) + day