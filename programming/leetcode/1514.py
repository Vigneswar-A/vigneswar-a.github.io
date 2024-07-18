class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        
        Start = 1
        flag = True
        while flag:
            
            flag = False
            sum = Start
            for i in nums:
                sum += i
                if sum < 1:
                    flag = True
                    Start += abs(sum)+1
                    break
                    
        return Start
        