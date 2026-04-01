class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # create adj list, then do a dfs and mark nodes as visited, if a node is not in 
        # visited, explore it

        adj = defaultdict(list)

        for a,b in edges:
            adj[a].append(b)
            adj[b].append(a)

        #create our dfs function, keep track of nodes we've visited
        visited = set()

        def dfs(node):
            if node in visited:
                return

            visited.add(node)
            for n in adj[node]:
                dfs(n)
        
        count = 0

        for i in range(n):
            if i not in visited:
                dfs(i)
                count += 1

        return count