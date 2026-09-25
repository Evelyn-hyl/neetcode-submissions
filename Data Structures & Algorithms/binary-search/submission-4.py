import math

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        nums_len = len(nums)

        return self.binary_search(nums, 0, nums_len-1, target)
    
    def binary_search(self, nums: List[int], left: int, right: int, target) -> int:
        if left > right:
            return -1

        mid = math.floor((left + right) / 2)

        if target == nums[mid]:
            return mid
        
        if target < nums[mid]:
            return self.binary_search(nums, left, mid - 1, target)
        else:
            return self.binary_search(nums, mid + 1, right, target)
