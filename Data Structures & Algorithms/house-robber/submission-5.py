class Solution:
    def rob(self, nums: List[int]) -> int:
        dfs_paths = defaultdict(int)

        def dfs(i):
            if i >= len(nums):
                return 0
            
            if not dfs_paths[i+2]:
                dfs_paths[i+2] = dfs(i+2)

            if not dfs_paths[i+1]:
                dfs_paths[i+1] = dfs(i+1)

            return max(nums[i] + dfs_paths[i+2], dfs_paths[i+1])
        
        return dfs(0)