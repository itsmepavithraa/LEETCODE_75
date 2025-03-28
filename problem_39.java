// Question:
// Given the root of a binary tree, return the values of the nodes you can see ordered from top to bottom when looking at the tree from the right side.

import java.util.*;

// Definition for a binary tree node.
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

class problem_39 {
    public List<Integer> rightSideView(TreeNode root) {
        List<Integer> result = new ArrayList<>();
        if (root == null) return result;
        
        Queue<TreeNode> queue = new LinkedList<>();
        queue.offer(root);
        
        while (!queue.isEmpty()) {
            int levelSize = queue.size();
            for (int i = 0; i < levelSize; i++) {
                TreeNode node = queue.poll();
                if (i == levelSize - 1) { // Last node in the level
                    result.add(node.val);
                }
                if (node.left != null) {
                    queue.offer(node.left);
                }
                if (node.right != null) {
                    queue.offer(node.right);
                }
            }
        }
        return result;
    }
    
    public static void main(String[] args) {
        // Constructing the following binary tree:
        //        1
        //       / \
        //      2   3
        //       \    \
        //        5    4
        TreeNode root = new TreeNode(1);
        root.left = new TreeNode(2);
        root.right = new TreeNode(3);
        root.left.right = new TreeNode(5);
        root.right.right = new TreeNode(4);

        problem_39 solution = new problem_39();
        System.out.println(solution.rightSideView(root)); // Output: [1, 3, 4]
    }
}

// Time Complexity: O(N) where N is the number of nodes in the tree. Each node is processed once.
// Space Complexity: O(N) due to storing nodes in the queue for BFS.
