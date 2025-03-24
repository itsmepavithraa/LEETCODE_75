// Question: Longest ZigZag Path in a Binary Tree
// Given the root of a binary tree, return the longest ZigZag path in the tree.

class TreeNode {
    int val;
    TreeNode left, right;

    TreeNode(int val) {
        this.val = val;
        this.left = null;
        this.right = null;
    }
}

class problem_37 {
    private int maxZigZag = 0; // Stores the maximum ZigZag length

    public int longestZigZag(TreeNode root) {
        if (root == null) return 0;
        dfs(root.left, false, 1); // Start from left child, next move should be right
        dfs(root.right, true, 1); // Start from right child, next move should be left
        return maxZigZag;
    }

    private void dfs(TreeNode node, boolean isLeft, int length) {
        if (node == null) return;
        maxZigZag = Math.max(maxZigZag, length);
        
        if (isLeft) {
            dfs(node.left, false, length + 1); // Move left, then right
            dfs(node.right, true, 1); // Reset length when switching direction
        } else {
            dfs(node.right, true, length + 1); // Move right, then left
            dfs(node.left, false, 1); // Reset length when switching direction
        }
    }

    public static void main(String[] args) {
        // Constructing the binary tree:
        //        1
        //       / \
        //      2   3
        //       \    \
        //        4    5
        //       /    /
        //      6    7
        //           \
        //            8
        //
        // Zigzag path: 1 → 3 → 5 → 7 → 8 (length 4)

        TreeNode root = new TreeNode(1);
        root.left = new TreeNode(2);
        root.right = new TreeNode(3);
        root.left.right = new TreeNode(4);
        root.right.right = new TreeNode(5);
        root.left.right.left = new TreeNode(6);
        root.right.right.left = new TreeNode(7);
        root.right.right.left.right = new TreeNode(8);

        problem_37 solution = new problem_37();
        System.out.println("Longest ZigZag Path Length: " + solution.longestZigZag(root));
        // Output: 4
    }
}

/*
Time Complexity: O(N)
- Each node is visited exactly once during the Depth-First Search (DFS).
- Each node contributes to recursive calls twice (once for left, once for right).
- Therefore, the overall time complexity is **O(N)** where N is the number of nodes.

Space Complexity: O(H)
- The recursion depth is at most the height of the tree.
- In a balanced tree, H = O(log N), while in a skewed tree, H = O(N).
- The additional space used by function call stack is **O(H)**.
*/
