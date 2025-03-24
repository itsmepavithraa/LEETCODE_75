// Question: Count Good Nodes in Binary Tree

// Given a binary tree root, a node X in the tree is named "good" 
// if in the path from root to X there are no nodes with a value greater than X.
// Return the number of good nodes in the binary tree.

class TreeNode {
    int val;
    TreeNode left, right;

    TreeNode(int val) {
        this.val = val;
        this.left = null;
        this.right = null;
    }
}

public class problem_35 {
    private int goodCount = 0; // Initialize counter for good nodes

    public int goodNodes(TreeNode root) {
        dfs(root, root.val); // Start DFS with root's value as the initial max
        return goodCount; // Return total good nodes count
    }

    private void dfs(TreeNode node, int maxVal) {
        if (node == null) return; // Base case

        if (node.val >= maxVal) { // If current node value is greater than or equal to max seen so far
            goodCount++; // Count it as a good node
        }

        // Recur for left and right subtrees with updated max value
        dfs(node.left, Math.max(maxVal, node.val));
        dfs(node.right, Math.max(maxVal, node.val));
    }

    public static void main(String[] args) {
        // Constructing the following binary tree:
        //        3
        //       / \
        //      1   4
        //     /   / \
        //    3   1   5
        
        TreeNode root = new TreeNode(3);
        root.left = new TreeNode(1);
        root.right = new TreeNode(4);
        root.left.left = new TreeNode(3);
        root.right.left = new TreeNode(1);
        root.right.right = new TreeNode(5);

        problem_35 solution = new problem_35();
        System.out.println("Number of Good Nodes: " + solution.goodNodes(root)); // Output: 4
    }
}
