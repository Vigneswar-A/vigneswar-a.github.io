class Solution:
    def nextClosestTime(self, time: str) -> str:
        x = time
        time = datetime.time(*map(int, time.split(':')))
        res1 = 0
        res2 = 0
        for i in range(24):
            for j in range(60):
                current = datetime.time(i, j)
                if current > time and set(f"{current.hour:0>2}{current.minute:0>2}") <= set(x):
                    if res1 == 0:
                        res1 = current
                    res1 = min(current, res1)
                if set(f"{current.hour:0>2}{current.minute:0>2}") <= set(x):
                    if res2 == 0:
                        res2 = current
                    res2 = min(current, res2)
        
        return f"{res1.hour:0>2}:{res1.minute:0>2}" if res1 != 0 else f"{res2.hour:0>2}:{res2.minute:0>2}"
        