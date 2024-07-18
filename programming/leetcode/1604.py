class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        nums = sorted(Counter(arr).items() , key = lambda arr : arr[1])

        while k > 0:
            i , n = nums.pop(0)
            k -= n

        return len(nums) + (k != 0)
            
            
                
            