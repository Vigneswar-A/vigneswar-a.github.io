class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        
        days = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]
        
        def get_days(s):
            month, day = map(int, s.split('-'))
            return days[month-1] + day


        return max(min(map(get_days, [leaveAlice,leaveBob])) - max(map(get_days, [arriveBob, arriveAlice])) + 1, 0)
        