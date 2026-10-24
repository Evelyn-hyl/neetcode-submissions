from collections import defaultdict
from heapq import heappush, heappop
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        neighbors = defaultdict(list)
        # neighbors = { 1: [(2, 1), (4, 4)]}
        
        for u, v, w in times:
            neighbors[u].append((v, w))
        
        min_heap = [(0, k)] # (cumulative time, node)
        visited = set()
        total_time = 0

        while min_heap:
            time1, node1 = heappop(min_heap)
            if node1 in visited:
                continue

            visited.add(node1)
            total_time = time1

            for node2, time2 in neighbors[node1]:
                if node2 not in visited:
                    heappush(min_heap, (time1 + time2, node2))

        print(visited)
        
        return total_time if len(visited) == n else -1
                