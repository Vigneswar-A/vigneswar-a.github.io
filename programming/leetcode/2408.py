class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        
        learn_day = [0]*(n+delay) # number of people that learnt secret on day i
        sharers = [0]*(n+delay) # number of people that are ready to share secret on day i
        dp = [0] * n
        learn_day[0] = 1 # first person learns on day 0
        
        for day in range(n):
            sharers[day] += sharers[day-1] + learn_day[day-delay] - learn_day[day-forget]
            learn_day[day] += sharers[day]
            dp[day] = dp[day-1] + learn_day[day] - learn_day[day-forget]

        return dp[-1]%(1000000007)

        
            