class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pre_prod = [1] * n
        suf_prod = [1] * n
        res = [1] * n

        pre_prod[0] = nums[0]
        suf_prod[n-1] = nums[n-1]

        # Prefix Product
        for i in range(1, n):
            if (i-1 in range(n)):
                pre_prod[i] *= pre_prod[i-1]
            pre_prod[i] *= nums[i]

        # Suffix Product
        for i in range(n-2, -1, -1):
            if (i+1 in range(n)):
                suf_prod[i] *= suf_prod[i+1]
            suf_prod[i] *= nums[i]

        for i in range(n):
            if (i-1 in range(n)):
                res[i] *= pre_prod[i-1]
            if (i+1 in range(n)):
                res[i] *= suf_prod[i+1]
        
        return res