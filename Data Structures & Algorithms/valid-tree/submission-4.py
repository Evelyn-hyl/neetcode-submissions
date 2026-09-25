from collections import defaultdict, deque

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        
        visited = {0}
        q = deque()
        adj = {i:[] for i in range(n)}

        for e, f in edges:
            adj[e].append(f)
            adj[f].append(e)
        
        q.append([0, -1])

        while q:
            curr, parent = q.popleft()

            for neighbor in adj[curr]:

                if neighbor == parent:
                    continue
                
                if neighbor in visited:
                    return False
                
                visited.add(neighbor)
                q.append([neighbor, curr])
        
        return len(visited) == n
