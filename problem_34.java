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

/*
Problem Statement:
------------------
Given two binary trees `root1` and `root2`, return `true` if and only if their 
**leaf sequences** are the same.

A tree's **leaf sequence** is the list of its leaf values read from left to right.

A leaf node is a node with **no children**.

Example 1:
-----------
Input:
    root1 = [3,5,1,6,2,9,8,null,null,7,4]
    root2 = [3,5,1,6,7,4,2,null,null,null,null,null,null,9,8]

Output:
    true

Explanation:
    The leaf sequence of both trees is [6, 7, 4, 9, 8], which is identical.

Example 2:
-----------
Input:
    root1 = [1,2,3]
    root2 = [1,3,2]

Output:
    false

Explanation:
    The leaf sequence of the first tree is [2, 3], while the second tree has [3, 2].
    Since they are different, the output is false.

Constraints:
------------
- The number of nodes in both trees is in the range **[1, 200]**.
- The values of tree nodes are in the range **[0, 200]**.

*/

class Solution {
    public boolean leafSimilar(TreeNode root1, TreeNode root2) {
        List<Integer> leaf1 = new ArrayList<>();
        List<Integer> leaf2 = new ArrayList<>();
        
        getLeafSequence(root1, leaf1);
        getLeafSequence(root2, leaf2);
        
        return leaf1.equals(leaf2);
    }

    private void getLeafSequence(TreeNode root, List<Integer> result) {
        if (root == null) return;
        if (root.left == null && root.right == null) { // If it's a leaf node
            result.add(root.val);
        }
        if (root.left != null) {
            getLeafSequence(root.left, result);
        }
        if (root.right != null) {
            getLeafSequence(root.right, result);
        }
    }

    /*
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
    */
}

public class problem_34 {
    public static void main(String[] args) {
        // Creating test case trees
        
        // Tree 1: [3,5,1,6,2,9,8,null,null,7,4]
        TreeNode root1 = new TreeNode(3);
        root1.left = new TreeNode(5);
        root1.right = new TreeNode(1);
        root1.left.left = new TreeNode(6);
        root1.left.right = new TreeNode(2);
        root1.left.right.left = new TreeNode(7);
        root1.left.right.right = new TreeNode(4);
        root1.right.left = new TreeNode(9);
        root1.right.right = new TreeNode(8);

        // Tree 2: [3,5,1,6,7,4,2,null,null,null,null,null,null,9,8]
        TreeNode root2 = new TreeNode(3);
        root2.left = new TreeNode(5);
        root2.right = new TreeNode(1);
        root2.left.left = new TreeNode(6);
        root2.left.right = new TreeNode(7);
        root2.right.left = new TreeNode(4);
        root2.right.right = new TreeNode(2);
        root2.right.right.left = new TreeNode(9);
        root2.right.right.right = new TreeNode(8);

        Solution solution = new Solution();
        System.out.println("Are the trees leaf-similar? " + solution.leafSimilar(root1, root2));
        // Output: true
    }
}
