# Question: Path Sum III
# Given the root of a binary tree and an integer targetSum, return the number of paths 
# where the sum of the values along the path equals targetSum.

from typing import Optional
from collections import defaultdict

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def dfs(root, ps):
            if not root:
                return
            cs = ps + root.val  # Compute current sum
            x = cs - targetSum   # Check if (current sum - target) exists in freq
            if x in freq:
                self.count += freq[x]  # If exists, add to count
            freq[cs] += 1  # Store current sum in the hashmap

            dfs(root.left, cs)  # Traverse left subtree
            dfs(root.right, cs) # Traverse right subtree

            freq[cs] -= 1  # Backtrack to remove current sum from path

        self.count = 0
        freq = defaultdict(int)  # Dictionary to store prefix sum frequencies
        freq[0] = 1  # Initialize prefix sum hashmap
        dfs(root, 0) # Start DFS traversal

        return self.count

# Example Test Case
if __name__ == "__main__":
    # Constructing the following binary tree:
    #         10
    #        /  \
    #       5   -3
    #      / \    \
    #     3   2    11
    #    / \   \
    #   3  -2   1
    root = TreeNode(10)
    root.left = TreeNode(5)
    root.right = TreeNode(-3)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(2)
    root.right.right = TreeNode(11)
    root.left.left.left = TreeNode(3)
    root.left.left.right = TreeNode(-2)
    root.left.right.right = TreeNode(1)

    targetSum = 8
    solution = Solution()
    print("Number of Paths with Sum {}: {}".format(targetSum, solution.pathSum(root, targetSum)))  
    # Output: 3

"""
Time Complexity: O(N)
- Each node is visited exactly once in the Depth-First Search (DFS).
- Lookup and insertion in the hashmap (freq dictionary) takes O(1) on average.
- Overall, the time complexity is O(N), where N is the number of nodes in the tree.

Space Complexity: O(H)
- The hashmap stores prefix sums, which in the worst case (all unique sums) can be O(N).
- The recursion depth is O(H), where H is the height of the tree.
  - Worst-case (skewed tree): O(N)
  - Best-case (balanced tree): O(log N)
- Overall, the space complexity is O(H), where H is the height of the tree.
"""
