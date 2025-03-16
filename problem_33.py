# LeetCode 104: Maximum Depth of Binary Tree

"""
Question:
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path 
from the root node down to the farthest leaf node.

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: 3

Example 2:
Input: root = [1,null,2]
Output: 2
"""

# Definition for a binary tree node.
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

# Example usage:
def main():
    """
    Example Tree:
        3
       / \
      9   20
         /  \
        15   7

    Expected Output: 3
    """
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    solution = Solution()
    print("Maximum Depth of Binary Tree:", solution.maxDepth(root))

if __name__ == "__main__":
    main()

"""
Time Complexity: O(N) - We visit each node once.
Space Complexity: O(H) - Where H is the height of the tree (O(log N) for balanced trees, O(N) for skewed trees).
"""
