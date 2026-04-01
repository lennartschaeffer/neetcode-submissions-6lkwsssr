class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # create adjancency list
        adj = defaultdict(list)
        for a,b in edges:
            adj[a].append(b)
            adj[b].append(a)

        path = set()

        # 0 : 1
        # 1 : 2,3,4
        # 2 : 3

        def dfs(root, parent):
            if root in path:
                return False
            
            path.add(root)

            for n in adj[root]:
                if n != parent:
                    if not dfs(n, root):
                        return False
            
            return True

        return dfs(0, -1) and len(edges) == n-1
        


