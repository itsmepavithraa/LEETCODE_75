# Question:
# Given the root of a binary tree, return the values of the nodes you can see ordered from top to bottom when looking at the tree from the right side.

# Import necessary modules
from collections import deque
from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:  # No root - tree empty 
            return []  # return empty list
        
        queue = deque([root])  # stores nodes for BFS
        result = []  # rightmost node of each level
        
        while queue:  # run until the queue is empty
            level_size = len(queue)  # no. of nodes in current level
            for i in range(level_size):  # loop through all the nodes in the current level
                node = queue.popleft()  # remove the front node
                if i == level_size - 1:  # Last node in the level
                    result.append(node.val)
                if node.left:  # if node has left child, add it to queue
                    queue.append(node.left)
                if node.right:  # if node has right child, add it to queue
                    queue.append(node.right)
        
        return result  # return right side view

# Example usage:
# Constructing the following binary tree:
#        1
#       / \
#      2   3
#       \    \
#        5    4
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.right = TreeNode(5)
root.right.right = TreeNode(4)

solution = Solution()
print(solution.rightSideView(root))  # Output: [1, 3, 4]

# Time Complexity: O(N) where N is the number of nodes in the tree. Each node is processed once.
# Space Complexity: O(N) due to storing nodes in the queue for BFS.
