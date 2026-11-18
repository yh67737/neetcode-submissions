class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        row=len(grid)
        col=len(grid[0])
        INF=2147483647
        queue=collections.deque()
        for i in range(row):
            for j in range(col):
                if grid[i][j]==0:
                    queue.append((i,j))
        while queue:
            r,c=queue.popleft()
            for i,j in [(1,0),(-1,0),(0,1),(0,-1)]:
                nr=r+i
                nc=c+j
                if nr<0 or nr>=row or nc<0 or nc>=col or grid[nr][nc]==-1:
                    continue
                if grid[nr][nc]!=INF:
                    continue
                grid[nr][nc]=grid[r][c]+1
                queue.append((nr,nc))



