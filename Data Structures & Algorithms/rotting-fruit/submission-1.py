class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        row=len(grid)
        col=len(grid[0])
        count=0
        queue=collections.deque()
        for i in range(row):
            for j in range(col):
                if grid[i][j]==1:
                    count+=1
                if grid[i][j]==2:
                    queue.append((i,j))
        if count==0:
            return 0
        rcount=0
        mini=0
        while queue:
            lev=len(queue)
            mini+=1
            for i in range(lev):
                r,c=queue.popleft()
                for dr,dc in [(1,0),(-1,0),(0,1),(0,-1)]:
                    nr=r+dr
                    nc=c+dc
                    if nr<0 or nr>=row or nc<0 or nc>=col or grid[nr][nc]==0 or grid[nr][nc]==2:
                        continue
                    grid[nr][nc]=2
                    queue.append((nr,nc))
                    rcount+=1
                    if rcount==count:
                        return mini
        return -1

                

