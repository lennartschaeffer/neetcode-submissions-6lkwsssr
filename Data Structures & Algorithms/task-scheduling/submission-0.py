
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = {}
        for t in tasks:
            freq[t] = freq.get(t, 0) - 1

        h = list(freq.values())
        heapq.heapify(h)
        q = deque()
        time = 0
        # h = [-2] t = 2
        # 2
        # q= [[-1,3], [-1,4]]
        
        while len(h) or len(q):
            if len(q) and q[0][1] <= time:
                front, _ = q.popleft()
                heapq.heappush(h,front)
            if not len(h):
                time += 1
            if len(h):
                top = -heapq.heappop(h)
                time += 1
                if top > 1:
                    q.append((-top+1, time+n))

        return time


        


        
        

