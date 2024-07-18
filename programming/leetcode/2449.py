class Solution:
    def maximumRobots(self, chargeTimes: List[int], runningCosts: List[int], budget: int) -> int:
        n = len(chargeTimes)
        st = [0]*n + chargeTimes
        prefix = [*accumulate(runningCosts)]
        
        for i in range(n-1,-1,-1):
            st[i] = max(st[2*i] , st[2*i+1])

        def get_cost(l,r):
            l += n
            r += n
            res = 0
            while l <= r:
                if l % 2:
                    res = max(res, st[l])
                    l += 1
                if r % 2 == 0:
                    res = max(res, st[r])
                    r -= 1
                l //= 2
                r //= 2

            return res
       
        res = 0
        left = right = 0
        while left < n and right < n:
            if left > right:
                right += 1
                continue
            sums = ((prefix[right]-prefix[left-1]) if left else prefix[right])
            cost = get_cost(left,right) + (right-left+1)*(sums)
            
            if cost <= budget:
                res = max(res , right-left+1)
                right += 1
            else:
                left += 1
                
            
            
        return res
            