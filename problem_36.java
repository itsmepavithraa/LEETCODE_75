// Question: Path Sum III
// Given the root of a binary tree and an integer targetSum, return the number of paths 
// where the sum of the values along the path equals targetSum.

import java.util.HashMap;

class TreeNode {
    int val;
    TreeNode left, right;

    TreeNode(int val) {
        this.val = val;
        this.left = null;
        this.right = null;
    }
}

class problem_36 {  
    private int count = 0; // Stores the number of valid paths

    public int pathSum(TreeNode root, int targetSum) {
        HashMap<Integer, Integer> prefixSumMap = new HashMap<>();
        prefixSumMap.put(0, 1); // Initialize prefix sum map with base case
        dfs(root, 0, targetSum, prefixSumMap); // Start DFS traversal
        return count;
    }

    private void dfs(TreeNode node, int currSum, int targetSum, HashMap<Integer, Integer> prefixSumMap) {
        if (node == null) return; // Base case

        currSum += node.val; // Compute current sum

        // Check if there exists a prefix sum that forms the target sum
        int requiredSum = currSum - targetSum;
        count += prefixSumMap.getOrDefault(requiredSum, 0);

        // Add current sum to prefix sum map
        prefixSumMap.put(currSum, prefixSumMap.getOrDefault(currSum, 0) + 1);

        // Recur for left and right subtrees
        dfs(node.left, currSum, targetSum, prefixSumMap);
        dfs(node.right, currSum, targetSum, prefixSumMap);

        // Backtrack: Remove current sum from prefix sum map
        prefixSumMap.put(currSum, prefixSumMap.get(currSum) - 1);
    }

    public static void main(String[] args) {
        // Constructing the following binary tree:
        //         10
        //        /  \
        //       5   -3
        //      / \    \
        //     3   2    11
        //    / \   \
        //   3  -2   1

        TreeNode root = new TreeNode(10);
        root.left = new TreeNode(5);
        root.right = new TreeNode(-3);
        root.left.left = new TreeNode(3);
        root.left.right = new TreeNode(2);
        root.right.right = new TreeNode(11);
        root.left.left.left = new TreeNode(3);
        root.left.left.right = new TreeNode(-2);
        root.left.right.right = new TreeNode(1);

        int targetSum = 8;
        problem_36 solution = new problem_36();
        System.out.println("Number of Paths with Sum " + targetSum + ": " + solution.pathSum(root, targetSum));
        // Output: 3
    }
}

/*
Time Complexity: O(N)
- Each node is visited exactly once in the Depth-First Search (DFS).
- Lookup and insertion in the hashmap (prefixSumMap) takes O(1) on average.
- Overall, the time complexity is O(N), where N is the number of nodes in the tree.

Space Complexity: O(H)
- The hashmap stores prefix sums, which in the worst case (all unique sums) can be O(N).
- The recursion depth is O(H), where H is the height of the tree.
  - Worst-case (skewed tree): O(N)
  - Best-case (balanced tree): O(log N)
- Overall, the space complexity is O(H), where H is the height of the tree.
*/
