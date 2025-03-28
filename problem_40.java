// Question:
// Given the root of a binary tree, return the level (1-based index) with the maximum sum.
// If there are multiple levels with the same maximum sum, return the smallest level.

import java.util.*;

class TreeNode {
    int val;
    TreeNode left, right;
    
    TreeNode(int val) {
        this.val = val;
        this.left = null;
        this.right = null;
    }
}

class problem_40 {
    public int maxLevelSum(TreeNode root) {
        if (root == null) return 0;

        Queue<TreeNode> queue = new LinkedList<>();
        queue.offer(root);

        int maxLevel = 1, level = 1, maxSum = Integer.MIN_VALUE;

        while (!queue.isEmpty()) {
            int levelSize = queue.size();
            int levelSum = 0;

            for (int i = 0; i < levelSize; i++) {
                TreeNode node = queue.poll();
                levelSum += node.val;

                if (node.left != null) queue.offer(node.left);
                if (node.right != null) queue.offer(node.right);
            }

            if (levelSum > maxSum) {
                maxSum = levelSum;
                maxLevel = level;
            }

            level++;
        }

        return maxLevel;
    }

    public static void main(String[] args) {
        // Constructing the binary tree:
        //         1
        //       /   \
        //      7     0
        //     / \     \
        //    7  -8     9

        TreeNode root = new TreeNode(1);
        root.left = new TreeNode(7);
        root.right = new TreeNode(0);
        root.left.left = new TreeNode(7);
        root.left.right = new TreeNode(-8);
        root.right.right = new TreeNode(9);

        problem_40 solution = new problem_40();
        System.out.println(solution.maxLevelSum(root)); // Output: 3
    }
}

// Time Complexity: O(N) where N is the number of nodes in the tree.
// Space Complexity: O(W) where W is the maximum width of the tree.
