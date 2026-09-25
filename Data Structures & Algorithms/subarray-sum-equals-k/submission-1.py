class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # prefix_sum : dict[int] = [2, 1, 2, 4]
        prefix_sum = defaultdict(int, {0: 1})
        curr_sum = 0
        result = 0

        for num in nums:
            curr_sum += num

            if prefix_sum[curr_sum - k]:
                result += prefix_sum[curr_sum - k]
            
            prefix_sum[curr_sum] += 1
        
        return result

