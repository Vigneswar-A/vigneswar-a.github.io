class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        return sum((('Push',) if i in target else ('Push' , 'Pop') for i in range(1 , max(target) + 1)) , ())