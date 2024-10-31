class Solution {
    public int[][] restoreMatrix(int[] rowSum, int[] colSum) {
        int n = rowSum.length;
        int m = colSum.length;
        int[][] res = new int[n][m];
        for (int i = 0; i < n; i++)
        {
            for (int j = 0; j < m; j++)
            {
                res[i][j] = 0;
            }
        }
        
        while(true)
        {
            int minIdx = 0;
            boolean isRow = true;
            for (int i = 0; i < Math.max(n, m); i++)
            {
                if (isRow)
                {
                    if (i < n && (rowSum[minIdx] == 0 || (rowSum[i] != 0 && rowSum[i] < rowSum[minIdx])))
                    {
                        minIdx = i;
                    }
                    if (i < m && (rowSum[minIdx] == 0 || (colSum[i] != 0 && colSum[i] < rowSum[minIdx])))
                    {
                        minIdx = i;
                        isRow = false;
                    }
                }
                else
                {
                    if (i < m && (colSum[minIdx] == 0  || (colSum[i] != 0 && colSum[i] < colSum[minIdx])))
                    {
                        minIdx = i;
                    }
                    if (i < n && (colSum[minIdx] == 0  || (rowSum[i] != 0 && rowSum[i] < colSum[minIdx])))
                    {
                        minIdx = i;
                        isRow = true;
                    }
                    
                }
            }
            
        
            if ((isRow && rowSum[minIdx] == 0) || !isRow && colSum[minIdx] == 0)
            {
                break;
            }
            
            if (isRow){
                int minCol = 0;
                for(int j = 0; j < m; j++)
                {
                    if (colSum[minCol] == 0 || (colSum[j] != 0 && colSum[j] < colSum[minCol]))
                    {
                        minCol = j;
                    }
                }
                res[minIdx][minCol] = rowSum[minIdx];
                colSum[minCol] -= rowSum[minIdx];
                rowSum[minIdx] = 0;
            }
                else{
                    int minRow = 0;
                    for(int j = 0; j < n; j++)
                    {
                        if (rowSum[minRow] == 0 || (rowSum[j] != 0 && rowSum[j] < rowSum[minRow]))
                        {
                            minRow = j;
                        }
                    }
                    res[minRow][minIdx] = colSum[minIdx];
                    rowSum[minRow] -= colSum[minIdx];
                    colSum[minIdx] = 0;
                }    
        }
        
        return res;
    }
}
