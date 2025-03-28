# Question:
# Given the root of a Binary Search Tree (BST) and an integer value,
# return the subtree rooted with that node. If the value does not exist, return None.

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None or root.val == val:
            return root  # Stop if found or tree is empty
        if val < root.val:
            return self.searchBST(root.left, val)  
        return self.searchBST(root.right, val)    

# Example Usage:
if __name__ == "__main__":
    # Constructing the BST:
    #         4
    #       /   \
    #      2     7
    #     / \   
    #    1   3   

    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(7)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)

    solution = Solution()
    result = solution.searchBST(root, 2)
    if result:
        print("Subtree rooted at:", result.val)  # Output: 2
    else:
        print("Value not found")

# Time Complexity: O(H) where H is the height of the BST (O(log N) for balanced BST, O(N) for skewed BST).
# Space Complexity: O(H) due to recursive stack calls.
