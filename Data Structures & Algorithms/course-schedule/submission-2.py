class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pre_map = { i:[] for i in range(numCourses)}

        for prereq in prerequisites:
            if prereq[0] == prereq[1]:
                return False
            pre_map[prereq[0]].append(prereq[1])

        visit = set()

        def dfs(crs: int):
            if crs in visit:
                return False
            
            if pre_map[crs] == []:
                return True
            
            visit.add(crs)
            
            for pre in pre_map[crs]:
                if not dfs(pre): return False
            
            visit.remove(crs)
            pre_map[crs] = []
            return True
        
        for i in range(numCourses):
            if not dfs(i): return False
        return True