class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        # map course to prereq, dfs kee

        courseToPre = defaultdict(list)

        for c,p in prerequisites:
            courseToPre[c].append(p)

        res = []
        valid = set()
        visited = set()

        def dfs(c):
            if c in visited:
                return False
            if c in valid:
                return True

            visited.add(c)
            for p in courseToPre[c]:
                if not dfs(p):
                    return False

            visited.remove(c)
            res.append(c)
            valid.add(c)
            courseToPre[c] = []
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return []
            

        return res
        

