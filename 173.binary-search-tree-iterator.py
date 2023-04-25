#
# @lc app=leetcode id=173 lang=python3
#
# [173] Binary Search Tree Iterator
#

from collections import deque

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.stack = deque([root])

        while root.left:
            root = root.left
            self.stack.append(root)


    def next(self) -> int:
        current_node = self.stack.pop()
        element_to_return = current_node.val

        if current_node.right:
            current_node = current_node.right
            self.stack.append(current_node)

            while current_node.left:
                current_node = current_node.left
                self.stack.append(current_node)

        return element_to_return

    def hasNext(self) -> bool:

        if not self.stack:
            return False
        return True


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
# @lc code=end

