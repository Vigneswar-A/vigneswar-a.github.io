class Solution:
    def maximumTime(self, time: str) -> str:
        
        for hr in range(23, -1, -1):
            for min in range(59, -1, -1):
                test_time = f"{hr:0>2}:{min:0>2}"
                if all(d1 == d2 for d1,d2 in zip(time, test_time) if d1 != "?"):
                    return test_time        