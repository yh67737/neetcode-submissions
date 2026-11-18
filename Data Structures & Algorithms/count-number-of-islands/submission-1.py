class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row=len(grid)
        col=len(grid[0])
        directions=[(1,0),(-1,0),(0,1),(0,-1)]
        ans=0
        def find(grid,i,j):
            if i<0 or i>=row or j<0 or j>=col or grid[i][j]=="0":
                    return
            grid[i][j]="0"
            for dr,dc in directions:
                nr=i+dr
                nc=j+dc
                find(grid,nr,nc)
        for i in range(row):
            for j in range(col):
                if grid[i][j]=="1":
                    ans+=1
                    find(grid,i,j)
        return ans

            
