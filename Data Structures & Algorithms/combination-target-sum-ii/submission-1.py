class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        res = []

        def backtrack(start, path):
            s = sum(path) 
            if s > target:
                return
            if s == target:
                p = sorted(path[:])
                if p not in res:
                    res.append(p)
            
            for i in range(start,len(candidates)):
                path.append(candidates[i])
                backtrack(i + 1, path)
                path.pop()

        backtrack(0,[])

        return res