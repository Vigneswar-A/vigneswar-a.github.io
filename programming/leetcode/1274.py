class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        return abs((datetime.datetime(*map(int,date2.split('-')))-datetime.datetime(*map(int,date1.split('-')))).days)
        