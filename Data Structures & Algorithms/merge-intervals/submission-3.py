class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = []
        res.append(intervals[0])

        # [[1,3],[1,5],[6,7]]
        # [[1,3]]

        for i in range(1,len(intervals)):
            # check if the last ivl's end time is > current ivl start time
            if res[-1][1] >= intervals[i][0]:
                #merge, ie take the max of the two intervals' end time
                res[-1] = [res[-1][0], max(intervals[i][1], res[-1][1])]
            else:
                res.append(intervals[i])
        
        return res