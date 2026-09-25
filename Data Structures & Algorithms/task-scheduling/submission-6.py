import heapq
from collections import deque

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if n == 0:
            return len(tasks)
        
        num_tasks = [0] * 26

        for task in tasks:
            num_tasks[ord(task) - ord("A")] += 1
        
        most_freq = max(num_tasks)
        num_most_freq = num_tasks.count(most_freq)
        
        time = (most_freq - 1) * (n + 1) + num_most_freq
        
        return max(len(tasks), time)


