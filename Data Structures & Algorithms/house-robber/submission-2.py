class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1:
            return nums[0]

        dp = []
        
        for i in range(n):
            if i == 0 or i == 1:
                dp.append(nums[i])
                continue
            
            if i - 2 >= 0 and i - 3 >= 0:
                dp.append(nums[i] + max(dp[i - 2], dp[i - 3]))
            else:
                dp.append(nums[i] + dp[i - 2])
            
        return max(dp[-1], dp[-2])