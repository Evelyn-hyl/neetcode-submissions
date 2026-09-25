from collections import deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereq_targets = {c:[] for c in range(numCourses)}
        in_degree = {c:0 for c in range(numCourses)}
        q = deque()
        result = []

        for dst, src in prerequisites:
            prereq_targets[src].append(dst)
            in_degree[dst] += 1

        for i in in_degree.keys():
            if in_degree[i] == 0:
                q.append(i)
        
        if not q:
            return []

        while q:
            q_len = len(q)

            for _ in range(q_len):
                course = q.popleft()
                
                for dst in prereq_targets[course]:
                    in_degree[dst] -= 1
                    if in_degree[dst] == 0:
                        q.append(dst)
                
                result.append(course)
        
        emptied = all(values == 0 for values in in_degree.values())

        return result if emptied else []

