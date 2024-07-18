class Solution:
    def findPairs(self, nums, k):
        if k==0:return sum(i>1 for i in collections.Counter(nums).values())
        Set=set(nums)
        return sum(x+k in Set for x in Set)