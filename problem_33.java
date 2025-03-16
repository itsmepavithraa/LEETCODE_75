// LeetCode 104: Maximum Depth of Binary Tree

/*
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
*/

class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;

    TreeNode(int val) {
        this.val = val;
        this.left = null;
        this.right = null;
    }
}

class Solution {
    public int maxDepth(TreeNode root) {
        if (root == null) {
            return 0;
        }
        return 1 + Math.max(maxDepth(root.left), maxDepth(root.right));
    }
}

public class problem_33 {
    public static void main(String[] args) {
        /*
        Example Tree:
            3
           / \
          9   20
             /  \
            15   7

        Expected Output: 3
        */
        
        TreeNode root = new TreeNode(3);
        root.left = new TreeNode(9);
        root.right = new TreeNode(20);
        root.right.left = new TreeNode(15);
        root.right.right = new TreeNode(7);

        Solution solution = new Solution();
        System.out.println("Maximum Depth of Binary Tree: " + solution.maxDepth(root));
    }
}

/*
Time Complexity: O(N) - We visit each node once.
Space Complexity: O(H) - Where H is the height of the tree (O(log N) for balanced trees, O(N) for skewed trees).
*/
