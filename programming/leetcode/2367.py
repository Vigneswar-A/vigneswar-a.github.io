class Solution:
    def minimumLines(self, stockPrices: List[List[int]]) -> int:
        if len(stockPrices) <= 1:
            return 0
        stockPrices.sort()
        res = 1
        for i in range(1, len(stockPrices)-1):
            if (stockPrices[i+1][1]-stockPrices[i][1])*(stockPrices[i][0]-stockPrices[i-1][0]) != (stockPrices[i+1][0]-stockPrices[i][0])*(stockPrices[i][1]-stockPrices[i-1][1]):
                res += 1

        return res 

        