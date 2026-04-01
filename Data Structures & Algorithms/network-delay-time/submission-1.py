class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # create my adj list, tuple (neighbour, time)

        adj = defaultdict(list)

        for a,b,c in times:
            adj[a].append((b,c))

        # a bfs, starting at k
        seen = set()
        h = []
        heapq.heappush(h,(0,k))
        seen.add(k)
        
        while h:
            time,node = heapq.heappop(h)
            seen.add(node)
            print(node,time, adj[node])
            print(seen)
            for nb,t in adj[node]:
                if nb not in seen:
                    heapq.heappush(h,(time + t, nb))
                    

            if len(seen) == n:
                return time

        return -1
            
