class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        sumMat = [[0 for i in range(len(mat[0]))] for j in range(len(mat))]
        
        sumMat[0][0] = mat[0][0]
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if i == 0 and j > 0:
                    sumMat[i][j] = sumMat[i][j-1] + mat[i][j]
                    continue
                elif i > 0 and j == 0:
                    sumMat[i][j] = sumMat[i-1][j] + mat[i][j]
                    continue
                elif i != 0 and j != 0:
                    sumMat[i][j] = sumMat[i-1][j] + sumMat[i][j-1] - sumMat[i-1][j-1] + mat[i][j]
          
        output = [[0 for i in range(len(mat[0]))] for j in range(len(mat))]
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                max_i = i+k if i+k < len(mat) else len(mat)-1
                max_j = j+k if j+k < len(mat[0]) else len(mat[0])-1
                
                Max = sumMat[max_i][max_j] 
                both = 0
                if i-k > 0:  
                    Max -= sumMat[i-k-1][max_j]
                    both+=1
                if j-k > 0:
                    Max -= sumMat[max_i][j-k-1]
                    both+=1
                if both > 1:
                    Max += sumMat[i-k-1][j-k-1]
                output[i][j] = Max
        return output