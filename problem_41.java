// Question:
// Given the root of a Binary Search Tree (BST) and an integer value,
// return the subtree rooted with that node. If the value does not exist, return null.


class TreeNode {
    int val;
    TreeNode left, right;
    
    TreeNode(int val) {
        this.val = val;
        this.left = null;
        this.right = null;
    }
}

class problem_41 {
    public TreeNode searchBST(TreeNode root, int val) {
        if (root == null || root.val == val) {
            return root; // Return node if found or return null if not present
        }
        return (val < root.val) ? searchBST(root.left, val) : searchBST(root.right, val);
    }

    public static void main(String[] args) {
        // Constructing the BST:
        //         4
        //       /   \
        //      2     7
        //     / \   
        //    1   3   

        TreeNode root = new TreeNode(4);
        root.left = new TreeNode(2);
        root.right = new TreeNode(7);
        root.left.left = new TreeNode(1);
        root.left.right = new TreeNode(3);

        problem_41 solution = new problem_41();
        TreeNode result = solution.searchBST(root, 2);
        if (result != null) {
            System.out.println("Subtree rooted at: " + result.val); // Output: 2
        } else {
            System.out.println("Value not found");
        }
    }
}

// Time Complexity: O(H) where H is the height of the BST (O(log N) for balanced BST, O(N) for skewed BST).
// Space Complexity: O(H) due to recursive stack calls.
