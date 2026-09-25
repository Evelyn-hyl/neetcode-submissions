class Solution:
    def findMin(self, nums: List[int]) -> int:
        mini = nums[0]
        l, r = 0, len(nums) - 1

        while l <= r:
            if nums[l] <= nums[r]:
                mini = min(mini, nums[l])
                break

            m = (l + r) // 2
            if nums[l] <= nums[m]:   # If left half is sorted
                mini = min(mini, nums[l])
                l = m + 1
            else:                   # If right half is sorted
                mini = min(mini, nums[m])
                r = m - 1
        
        return mini