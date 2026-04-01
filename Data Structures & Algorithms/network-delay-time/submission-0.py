class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # create my adj list, tuple (neighbour, time)

        # k => dfs => backtrack since we want to find all possible solutions
        adj = defaultdict(list)

        for a,b,c in times:
            adj[a].append((b,c))

        times = {node: float("inf") for node in range(1,n+1)}

        def dfs(node,time):
            if time >= times[node]:
                return
            times[node] = time

            for nbr,weight in adj[node]:
                dfs(nbr, time + weight)

        dfs(k,0)
        res = max(times.values())
        if res >= float("inf"):
            return -1

        return res
