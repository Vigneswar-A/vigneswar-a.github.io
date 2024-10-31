class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        return sorted(nums, key=lambda s:int(''.join(map(str, map(mapping.__getitem__, map(int, str(s)))))))
       
        