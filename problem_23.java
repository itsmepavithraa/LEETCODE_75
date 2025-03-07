// LeetCode Problem: Equal Row and Column Pairs
// 
// **Problem Statement:**
// Given an `n x n` matrix `grid`, return the number of pairs `(ri, ci)` such that row `ri` and column `ci` are equal.
// 
// **Example:**
// ```
// Input: grid = [[3,2,1],[1,7,6],[2,7,7]]
// Output: 1
// Explanation: There is 1 pair where row and column are equal:
// - (0, 2): Row 0 -> [3, 2, 1], Column 2 -> [3, 2, 1]
// ```
//
// **Constraints:**
// - `n == grid.length`
// - `n == grid[i].length`
// - `1 <= n <= 200`
// - `1 <= grid[i][j] <= 10^5`

import java.util.HashMap;
import java.util.Map;

public class problem_23 {
    public int equalPairs(int[][] grid) {
        Map<String, Integer> rowCount = new HashMap<>();
        int count = 0;
        int n = grid.length;
        
        // Count the frequency of each row
        for (int[] row : grid) {
            String rowStr = arrayToString(row);
            rowCount.put(rowStr, rowCount.getOrDefault(rowStr, 0) + 1);
        }
        
        // Count matching columns
        for (int col = 0; col < n; col++) {
            int[] columnArray = new int[n];
            for (int row = 0; row < n; row++) {
                columnArray[row] = grid[row][col];
            }
            String colStr = arrayToString(columnArray);
            count += rowCount.getOrDefault(colStr, 0);
        }
        
        return count;
    }

    private String arrayToString(int[] array) {
        StringBuilder sb = new StringBuilder();
        for (int num : array) {
            sb.append(num).append(",");
        }
        return sb.toString();
    }

    // Time Complexity: O(n^2)
    // Space Complexity: O(n^2)

    // Example usage:
    public static void main(String[] args) {
        problem_23 sol = new problem_23();
        int[][] grid = {{3, 2, 1}, {1, 7, 6}, {2, 7, 7}};
        int result = sol.equalPairs(grid);
        System.out.println("Number of equal row and column pairs: " + result);
    }
}

// Output: Number of equal row and column pairs: 1

