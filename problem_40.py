# Question:
# Given the root of a binary tree, return the level (1-based index) with the maximum sum.
# If there are multiple levels with the same maximum sum, return the smallest level.

from typing import Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if not root: 
            return 0
        
        q = deque([root])
        max_level = 1
        level = 1
        max_sum = float('-inf')

        while q:
            level_sum = 0
            for _ in range(len(q)):
                node = q.popleft()
                level_sum += node.val

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            if level_sum > max_sum:
                max_sum = level_sum
                max_level = level

            level += 1

        return max_level

# Example Usage:
if __name__ == "__main__":
    # Constructing the binary tree:
    #         1
    #       /   \
    #      7     0
    #     / \     \
    #    7  -8     9

    root = TreeNode(1)
    root.left = TreeNode(7)
    root.right = TreeNode(0)
    root.left.left = TreeNode(7)
    root.left.right = TreeNode(-8)
    root.right.right = TreeNode(9)

    solution = Solution()
    print(solution.maxLevelSum(root))  # Output: 3

# Time Complexity: O(N) where N is the number of nodes in the tree.
# Space Complexity: O(W) where W is the maximum width of the tree.
