class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row=len(grid)
        col=len(grid[0])
        ans=0
        def dfs(i,j):
            if i<0 or i>=row or j<0 or j>=col or grid[i][j]=="0":
                return
            grid[i][j]="0"
            for d in [(1,0),(-1,0),(0,1),(0,-1)]:
                nr,nc=i+d[0],j+d[1]
                dfs(nr,nc)
            return
        for i in range(row):
            for j in range(col):
                if grid[i][j]=="1":
                    dfs(i,j)
                    ans+=1
        return ans
        