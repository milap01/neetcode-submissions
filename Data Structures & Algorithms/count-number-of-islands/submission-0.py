class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        n = len(grid)
        m = len(grid[0])

        vis = [[0]*m for _ in range(n)]

        def dfs(i,j):

            vis[i][j] = 1

            dx = [1,-1,0,0]
            dy = [0,0,1,-1]

            for z in range(4):

                ni = i + dx[z]
                nj = j + dy[z]

                if (0 <= ni < n) and (0 <= nj < m) and (not vis[ni][nj] )and grid[ni][nj] != "0":

                    dfs(ni,nj)
                
        comp = 0

        

        for i in range(n):

            for j in range(m):

                if (not vis[i][j]) and grid[i][j] != "0":

                    comp += 1

                    dfs(i,j)
        
        return comp




        