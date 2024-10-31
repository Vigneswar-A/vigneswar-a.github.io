class Solution {
    public int surfaceArea(int[][] grid) {
        
        int n = grid.length;
        int directions[][] = {{0, 1}, {1, 0}, {-1, 0}, {0, -1}};
        int res = 0;
        for (int i = 0; i < n; i++){
            for(int j = 0; j < n; j++)
            {
                if(grid[i][j] == 0) continue;
                for(int[] direction : directions)
                {
                    int x = direction[0];
                    int y = direction[1];
                    if (0 <= i+x && i+x < n && 0 <= j+y && j+y < n )
                    {
                        res += Math.max(0, grid[i][j]-grid[i+x][j+y]);
                    }
                    else{
                        res += grid[i][j];
                    }
                }
                res += 2;
            }
        }
        return res;
    }
}