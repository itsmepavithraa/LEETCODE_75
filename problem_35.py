# Question: Count Good Nodes in Binary Tree

# Given a binary tree root, a node X in the tree is named "good" 
# if in the path from root to X there are no nodes with a value greater than X.
# Return the number of good nodes in the binary tree.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.good = 0  # Initialize counter for good nodes
        
        def dfs(root, check):
            if root.val >= check:  # If current node value is greater than or equal to max seen so far
                self.good += 1  # Count it as a good node
            if root.left:
                dfs(root.left, max(check, root.val))  # Traverse left with updated max value
            if root.right:
                dfs(root.right, max(check, root.val))  # Traverse right with updated max value

        dfs(root, root.val)  # Start DFS from root with its value as the initial max
        return self.good  # Return the total count of good nodes

# Time Complexity: O(N), where N is the number of nodes in the tree (each node is visited once).
# Space Complexity: O(H), where H is the height of the tree (recursive call stack).
# In the worst case (skewed tree), H = N, leading to O(N) space complexity.
# In the best case (balanced tree), H = log N, leading to O(log N) space complexity.

# Example Test Case:
# Constructing the following binary tree:
#        3
#       / \
#      1   4
#     /   / \
#    3   1   5

root = TreeNode(3)
root.left = TreeNode(1)
root.right = TreeNode(4)
root.left.left = TreeNode(3)
root.right.left = TreeNode(1)
root.right.right = TreeNode(5)

solution = Solution()
print("Number of Good Nodes:", solution.goodNodes(root))  # Output: 4
