class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}
        length = len(nums)
        list = []

        for i in range(length):
            if nums[i] in hashMap:
                list = [hashMap[nums[i]], i]
                return list
            
            hashMap[target - nums[i]] = i
        
        return list