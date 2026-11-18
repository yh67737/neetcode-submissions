class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        row=len(grid)
        col=len(grid[0])
        maxa=0
        def dfs(grid,i,j):
            if i<0 or i>=row or j<0 or j>=col or grid[i][j]==0:
                return 0
            grid[i][j]=0
            ans=1
            for n in [(1,0),(-1,0),(0,1),(0,-1)]:
                nr,nc=i+n[0],j+n[1]
                ans+=dfs(grid,nr,nc)
            return ans
        for i in range(row):
            for j in range(col):
                if grid[i][j]==1:
                    a=dfs(grid,i,j)
                    maxa=max(maxa,a)
        return maxa

        
