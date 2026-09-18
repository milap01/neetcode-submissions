class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        graph = defaultdict(list)

        for edge in edges:

            u,v = edge[0],edge[1]

            graph[u].append(v)
            graph[v].append(u)

        comp = 0

        vis = [0]*(n+1)

        def dfs(node):

            vis[node] = 1

            for neigh in graph[node]:

                if not vis[neigh]:

                    dfs(neigh)

        for node in range(n):

            if not vis[node]:

                comp += 1

                dfs(node)
        



        if len(edges) == n-1 and comp == 1:

            return True
        else:

            return False
        