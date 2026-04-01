class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # dfs find the cycle
        adj = defaultdict(list)
        for a,b in edges:
            adj[a].append(b)
            adj[b].append(a)
        
        visited = set()
        res = []
        def dfs(node,parent):
            if node in visited:
                print("cycle")
                return True
            
            visited.add(node)
            print(visited)
            for n in adj[node]:
                if n != parent and dfs(n,node) == True:
                    return True
            
            return False

        for a,b in reversed(edges):
            visited.clear()
            cycle = dfs(a,b)
            print(cycle)
            if cycle and a in visited and b in visited:
                return [a,b]

        return []