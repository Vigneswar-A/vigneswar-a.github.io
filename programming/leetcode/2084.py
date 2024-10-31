class Solution:
    def numberOfWeeks(self, milestones: List[int]) -> int:
        total = sum(milestones)
        max_mile = max(milestones)
        
        
        return min(total, 2*(total-max_mile)+1)
        
        