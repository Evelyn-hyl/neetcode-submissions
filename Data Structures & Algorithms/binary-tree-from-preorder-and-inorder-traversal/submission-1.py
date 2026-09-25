# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        pre_ptr = 0
        
        inorder_dict = { val: i for i, val in enumerate(inorder)}

        def DFS(l, r):
            nonlocal pre_ptr

            if r < l:
                return None

            root_val = preorder[pre_ptr]
            pre_ptr += 1
            node = TreeNode(root_val)

            mid = inorder_dict[root_val]

            node.left = DFS(l, mid - 1)
            node.right = DFS(mid + 1, r)

            return node

        return DFS(0, len(inorder) - 1)




