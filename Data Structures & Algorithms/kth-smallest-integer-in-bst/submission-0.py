# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        k_count = k
        ptr = root.val

        def inorder_find_kth(node):
            nonlocal k_count, ptr
            if not node:
                return

            inorder_find_kth(node.left)

            if k_count == 0:
                return
            
            k_count -= 1

            if k_count == 0:
                ptr = node.val
                return
            
            inorder_find_kth(node.right)
        
        inorder_find_kth(root)
        return ptr