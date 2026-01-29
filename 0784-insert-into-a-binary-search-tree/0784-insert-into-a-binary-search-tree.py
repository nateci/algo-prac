# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        current = root
        if current is None:
            return TreeNode(val)

        if current.val > val:
            current.left = self.insertIntoBST(current.left, val)
        else:
            current.right = self.insertIntoBST(current.right, val)
        
        return current
        