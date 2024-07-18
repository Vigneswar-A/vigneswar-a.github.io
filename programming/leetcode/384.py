class Solution:

    def __init__(self, nums: List[int]):
        self.iterator = permutations(nums)
        self.perms = copy.copy(self.iterator)
        self.original = nums

    def reset(self) -> List[int]:
        return self.original
        
    def shuffle(self) -> List[int]:
        next_ = next(self.perms , None)
        
        if not next_:
            self.perms = copy.copy(self.iterator)
            next_ = next(self.perms , None)
            
        return next_