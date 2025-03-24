# Question: Longest ZigZag Path in a Binary Tree
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        def dfs(node, is_left, length):
            nonlocal max_zigzag
            if not node:
                return 
            max_zigzag = max(max_zigzag, length)
            if is_left:
                dfs(node.left, False, length + 1)  # Move left, then right
                dfs(node.right, True, 1)  # Reset length when switching side
            else:
                dfs(node.right, True, length + 1)  # Move right, then left
                dfs(node.left, False, 1)  # Reset length when switching side
        
        max_zigzag = 0
        dfs(root.left, False, 1)  # Start from left child  # Next move - Right
        dfs(root.right, True, 1)  # Start from right child # Next move - Left
        return max_zigzag

# Example Usage:
# Constructing the binary tree:
#        1
#       / \
#      2   3
#       \    \
#        4    5
#       /    /
#      6    7
#           \
#            8
#
# Zigzag path: 1 → 2 → 4 → 6 (length 3) or 1 → 3 → 5 → 7 → 8 (length 4)

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.right = TreeNode(4)
root.right.right = TreeNode(5)
root.left.right.left = TreeNode(6)
root.right.right.left = TreeNode(7)
root.right.right.left.right = TreeNode(8)

solution = Solution()
print("Longest ZigZag Path Length:", solution.longestZigZag(root))  # Output: 4

"""
Time Complexity: O(N)
- Each node is visited exactly once in the Depth-First Search (DFS).
- Each node contributes to recursive calls twice (once for left, once for right).
- Therefore, the overall time complexity is **O(N)** where N is the number of nodes.

Space Complexity: O(H)
- The recursion depth is at most the height of the tree.
- In a balanced tree, H = O(log N), while in a skewed tree, H = O(N).
- The additional space used by function call stack is **O(H)**.
"""
