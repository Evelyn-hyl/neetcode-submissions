class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        nums.sort()
        longest = 1
        curr_len = 1

        for i in range(1, len(nums)):
            if nums[i] == nums[i-1] + 1:
                curr_len += 1
            elif nums[i] == nums[i-1]:
                continue
            else:
                longest = max(longest, curr_len)
                curr_len = 1
        
        return max(longest, curr_len)