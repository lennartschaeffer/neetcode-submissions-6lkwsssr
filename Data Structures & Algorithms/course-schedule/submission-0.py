class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        courseToPre = defaultdict(list)
        for c,p in prerequisites:
            courseToPre[c].append(p)

        # (0,)
        # [[0,1],[1,2][2,3],[0,4]]
        # 0 : 1,4
        # 1 : 2
        # 2 : []
        # 3: []
        # 4: []
        path = set()
        def dfs(course):
            #search through the prereqs, if the course is in
            if course in path:
                return False
            if not len(courseToPre[course]):
                return True

            path.add(course)
            for p in courseToPre[course]:
                if not dfs(p):
                    return False

            path.remove(course)
            courseToPre[p] = []
            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return False

        return True


        


