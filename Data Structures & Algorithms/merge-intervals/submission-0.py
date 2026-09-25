class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # hashmap = { starting val : ending val }
        result = []
        intervals.sort()

        for interval in intervals:
            if result and interval[0] <= result[-1][1]:
                new_min = min(interval[0], result[-1][0])
                new_max = max(interval[1], result[-1][1])
                result[-1] = [new_min, new_max]
                continue
            
            result.append(interval)

        return result 
            
            
