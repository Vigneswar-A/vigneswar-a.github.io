class Solution:
    def haveConflict(self, event1: List[str], event2: List[str]) -> bool:

        time1s = datetime.time(*map(int, event1[0].split(":")))
        time1e = datetime.time(*map(int, event1[1].split(":")))
        time2s = datetime.time(*map(int, event2[0].split(":")))
        time2e = datetime.time(*map(int, event2[1].split(":")))

        if time1e < time2s:
            return False

        if time2e < time1s:
            return False

        return True

