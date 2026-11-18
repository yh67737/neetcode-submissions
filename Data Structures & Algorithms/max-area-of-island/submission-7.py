class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        row=len(grid)
        col=len(grid[0])
        ans=0
        def dfs(i,j):
            if i<0 or i>=row or j<0 or j>=col or grid[i][j]==0:
                return 0
            grid[i][j]=0
            area=1
            for r,c in [(1,0),(-1,0),(0,1),(0,-1)]:
                nr,nc=i+r,j+c
                area+=dfs(nr,nc)
            return area
        for i in range(row):
            for j in range(col):
                if grid[i][j]==1:
                    area=dfs(i,j)
                    ans=max(ans,area)
        return ans

            
            