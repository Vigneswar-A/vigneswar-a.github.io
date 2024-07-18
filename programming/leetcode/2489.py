class Solution:
    def sortArray(self, nums: List[int]) -> int:
        res = inf
        # Type 1
        for di,end in [(0,0), (-1,len(nums)-1)]:
            hashmap = {nums[i]:i for i in range(len(nums))}
            rem = {i for i in nums if hashmap[i] != i+di and i != 0}
        
            flag = True
            count = 0
            while flag and count < res:
                flag = False
                if hashmap[0] != end:
                    i = hashmap[0]-di
                elif rem:
                    i = rem.pop()
                    while rem and hashmap[i] == i+di:
                        i = rem.pop()
                else:
                    break
                while hashmap[i] != i+di:
                    hashmap[0], hashmap[i] = hashmap[i], hashmap[0]                
                    count += 1
                    flag = True
                    if hashmap[0] != i+di:
                        break

            res = min(res, count)
            
        return res