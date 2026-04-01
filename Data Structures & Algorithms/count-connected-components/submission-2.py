class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        adj = defaultdict(list)

        for a,b in edges:
            adj[a].append(b)
            adj[b].append(a)


        visited = set()

        def dfs(node, parent):
            if node in visited:
                return

            visited.add(node)

            for n in adj[node]:
                if n != parent:
                    dfs(n, node)

        count = 0

        for i in range(n):
            if i not in visited:
                dfs(i,-1)
                count += 1

        return count