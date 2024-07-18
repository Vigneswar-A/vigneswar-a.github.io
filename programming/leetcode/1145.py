class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        m, n = len(matrix), len(matrix[0])
        for row in matrix:
            for i in range(1, n):
                row[i] += row[i-1]
            row += [0]
        
        res = 0
        for i in range(n):
            for j in range(i, n):
                counts = Counter()
                curr_sum, counts[0] = 0, 1
                for k in range(m):
                    curr_sum += matrix[k][j] - matrix[k][i-1]
                    res += counts[curr_sum - target]
                    counts[curr_sum] += 1
        return res