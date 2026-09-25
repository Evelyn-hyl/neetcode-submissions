class Solution:
    def findMin(self, nums: List[int]) -> int:
        sol = Solution()
        l = 0
        r = len(nums) - 1
        
        return sol.binary_search(nums, l, r)
    
    def binary_search(self, nums, l, r) -> int:
        mid = (l + r) // 2

        if (nums[l] + nums[r]) // 2 == nums[mid]:
            return nums[l]
        else:
            left_min = self.binary_search(nums, l, mid)
            right_min = self.binary_search(nums, mid + 1, r)
            return min(left_min, right_min)