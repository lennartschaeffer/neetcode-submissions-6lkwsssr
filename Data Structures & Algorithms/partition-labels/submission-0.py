class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        """
            xyxxyzbzbbisl

        """

        lastSeen = {}

        for idx,c in enumerate(s):
            lastSeen[c] = idx
        
        start = 0
        end = 0
        res = []

        for idx,c in enumerate(s):
            end = max(end,lastSeen[c])
            size = end - start + 1
            if idx == end:
                res.append(size)
                start = idx + 1
        
        return res