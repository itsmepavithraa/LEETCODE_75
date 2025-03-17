from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

"""
Problem Statement:
------------------
Given two binary trees `root1` and `root2`, return `True` if and only if their 
**leaf sequences** are the same.

A tree's **leaf sequence** is the list of its leaf values read from left to right.

A leaf node is a node with **no children**.

Example 1:
-----------
Input:
    root1 = [3,5,1,6,2,9,8,None,None,7,4]
    root2 = [3,5,1,6,7,4,2,None,None,None,None,None,None,9,8]

Output:
    True

Explanation:
    The leaf sequence of both trees is [6, 7, 4, 9, 8], which is identical.

Example 2:
-----------
Input:
    root1 = [1,2,3]
    root2 = [1,3,2]

Output:
    False

Explanation:
    The leaf sequence of the first tree is [2, 3], while the second tree has [3, 2].
    Since they are different, the output is False.

Constraints:
------------
- The number of nodes in both trees is in the range **[1, 200]**.
- The values of tree nodes are in the range **[0, 200]**.

"""

class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        leaf1 = []
        leaf2 = []
        
        def getLeaf(root, result):
            if root is None:
                return
            if root.left is None and root.right is None:  # If it's a leaf node
                result.append(root.val)
            if root.left:
                getLeaf(root.left, result)
            if root.right:
                getLeaf(root.right, result)
        
        getLeaf(root1, leaf1)
        getLeaf(root2, leaf2)
        
        return leaf1 == leaf2

"""
Time Complexity Analysis:
-------------------------
- Each node is visited **once**, so the time complexity is **O(N + M)**, 
  where N and M are the number of nodes in `root1` and `root2`, respectively.

Space Complexity Analysis:
--------------------------
- We store leaf values in `leaf1` and `leaf2`, which at most contain **L** leaf nodes.
- The recursion stack in a **balanced tree** is **O(log N)** but in the worst case 
  (skewed tree), it is **O(N)**.
- The worst-case space complexity is **O(N + M)**.
"""

# Test case
if __name__ == "__main__":
    # Creating test case trees

    # Tree 1: [3,5,1,6,2,9,8,None,None,7,4]
    root1 = TreeNode(3, 
                     TreeNode(5, TreeNode(6), TreeNode(2, TreeNode(7), TreeNode(4))),
                     TreeNode(1, TreeNode(9), TreeNode(8)))

    # Tree 2: [3,5,1,6,7,4,2,None,None,None,None,None,None,9,8]
    root2 = TreeNode(3, 
                     TreeNode(5, TreeNode(6), TreeNode(7)),
                     TreeNode(1, TreeNode(4), TreeNode(2, TreeNode(9), TreeNode(8))))

    solution = Solution()
    print("Are the trees leaf-similar?", solution.leafSimilar(root1, root2))  
    # Output: True
