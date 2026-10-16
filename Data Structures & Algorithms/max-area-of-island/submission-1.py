from collections import defaultdict
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        def dfs(row,col,component):

            comp_size[component] += 1

            vis[row][col] = 1

            dx = [1,0,-1,0]
            dy = [0,1,0,-1]

            for i in range(4):

                nr = row + dx[i]
                nc = col + dy[i]

                if 0 <= nr < n and 0 <= nc < m and not vis[nr][nc] and grid[nr][nc] == 1:

                    dfs(nr,nc,component)

        component = 0

        n = len(grid)

        m = len(grid[0])

        vis = [[0]*m for _ in range(n)]

        comp_size = defaultdict(int)

        for r in range(n):

            for c in range(m):

                if not vis[r][c] and grid[r][c] == 1:

                    component += 1

                    dfs(r,c,component)

        
        if not comp_size:

            return 0
        
        mx_key = max(comp_size,key=comp_size.get)

        return comp_size[mx_key]
        