class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        row=len(grid)
        col=len(grid[0])
        ans=0
        def dfs(r,c):
            if r<0 or r>=row or c<0 or c>=col or grid[r][c]==0:
                return 0
            area=1
            grid[r][c]=0
            for i,j in [(1,0),(-1,0),(0,1),(0,-1)]:
                area+=dfs(r+i,c+j)
            return area
        for i in range(row):
            for j in range(col):
                if grid[i][j]==1:
                    area=dfs(i,j)
                    if area>ans:
                        ans=area
        return ans