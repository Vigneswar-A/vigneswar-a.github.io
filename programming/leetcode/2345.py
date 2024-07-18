class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        
        def get_mins(time):
            hour,mins = map(int, time.split(":"))
            return 60*hour + mins

        rem = get_mins(correct) - get_mins(current)
        
        i60,rem = divmod(rem, 60)
        i15,rem = divmod(rem, 15)
        i5,rem = divmod(rem, 5)
        i1,rem = divmod(rem, 1)
        
        return i1+i5+i15+i60