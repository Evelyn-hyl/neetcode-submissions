# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def recur_dfs(node: Optional[TreeNode], l_bound: int, r_bound) -> bool:
            if not node:
                return True

            if not (node.val > l_bound and node.val < r_bound):
                return False
            
            return recur_dfs(node.left, l_bound, node.val) and recur_dfs(node.right, node.val, r_bound)

        return recur_dfs(root, float('-inf'), float('inf'))
        

    

        
