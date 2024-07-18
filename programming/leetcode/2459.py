class Solution:
    def minNumberOfHours(self, initialEnergy: int, initialExperience: int, energy: List[int], experience: List[int]) -> int:
        
        my_exp = initialExperience
        hours = 0

        for eg,exp in zip(energy, experience):
            if my_exp <= exp:
                hours += exp-my_exp+1
                my_exp = exp+1
            my_exp += exp

        return hours + max(0, sum(energy) - initialEnergy + 1)


