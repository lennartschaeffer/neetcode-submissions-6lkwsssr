class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        """
            first check cycle in graph
            then topologically sort the answer

            we only want to compare a current word's characters to words that
            came before it. we dont care about the order within the word itself.
            
            for each char c in each word w, i want to create a directed edge between all previous characters in words at the index, since this character
            should come after it lexicographically
            if the characters are different, i just create the edge and break the loop from there, if they match, i want to continue comparing so i do
            nothing

        """

        adj = defaultdict(set)
        ind = defaultdict(int)
        chars = set()
        for i in range(len(words)):
            for j in range(len(words[i])):
                chars.add(words[i][j])

        for i in range(len(words)):
            for k in range(i):
                valid = False
                for j in range(len(words[i])):
                    if j >= len(words[k]): continue
                    if words[i][j] != words[k][j]:
                        valid = True
                        if words[i][j] not in adj[words[k][j]]:
                            ind[words[i][j]] += 1
                        adj[words[k][j]].add(words[i][j])
                        break
                if not valid and len(words[k]) > len(words[i]): return ""
                    
        # topological sort will also detect cycle
        # calcualte indegree of each node, then do bfs topo sort algorithm
        q = deque()
        res = []
        seen = set()
        for c in chars:
            if ind[c] == 0:
                q.append(c) 
                seen.add(c)
        if not len(q): return ""
        while q:
            val = q.popleft()
            res.append(val)
            for nbr in adj[val]:
                ind[nbr] -= 1
                if ind[nbr] == 0:
                    q.append(nbr)
                    seen.add(nbr)
        if len(seen) < len(chars):return ""
        return "".join(res)
        
                    


