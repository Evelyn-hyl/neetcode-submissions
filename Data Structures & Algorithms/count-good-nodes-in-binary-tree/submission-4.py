# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        good_nodes = 0

        def inorder(node, largest):
            nonlocal good_nodes

            if not node:
                return
            
            if node.val >= largest:
                good_nodes += 1
                print(node.val)
                largest = node.val
            
            inorder(node.left, largest)
            inorder(node.right, largest)

        inorder(root, root.val - 1)

        return good_nodes

        