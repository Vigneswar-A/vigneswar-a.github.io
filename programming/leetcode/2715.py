class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        
        ones = min(numOnes, k)
        zeros = min(numZeros, k-ones)
        negs = min(numNegOnes, k-zeros-ones)
        
        return ones - negs