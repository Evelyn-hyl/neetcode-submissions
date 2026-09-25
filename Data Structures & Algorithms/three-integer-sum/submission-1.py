class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        triplets = set()
        res = []
        j_plus_k = []

        for i in range(n):
            diff = 0 - nums[i]
            j_plus_k.append(diff)
        
        l, r = 0, n-1

        for i in range(n):
            while l < r:
                if l == i:
                    l += 1
                    continue
                if r == i:
                    r -= 1
                    continue
                
                if nums[l] + nums[r] < j_plus_k[i]:
                    l += 1
                elif nums[l] + nums[r] > j_plus_k[i]:
                    r -= 1
                else:
                    triplet = tuple(sorted([nums[i], nums[l], nums[r]]))
                    if triplet not in res:
                        res.append(triplet)
                        triplets.add(triplet)
                    l += 1
            l = 0
            r = n-1

        return res

            
