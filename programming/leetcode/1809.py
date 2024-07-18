class Solution:
    def solve(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        n = len(nums)
        t = isqrt(n)
        
        prefixes = defaultdict(lambda : defaultdict(list))
        for y in range(1, t):
            for start in range(y):
                prefixes[y][start] = [0]
                for i in range(start, len(nums), y):
                    prefixes[y][start].append(prefixes[y][start][-1]+nums[i])
                
        def get_sum(x, y):
            return sum(nums[i] for i in range(x, len(nums), y))%(10**9+7)
        
        res = []
        for x,y in queries:
            if y < t:
                res.append((prefixes[y][x%y][-1] - prefixes[y][x%y][x//y])%(10**9+7))
            else:
                res.append(get_sum(x,y))
        return res
                
            
        