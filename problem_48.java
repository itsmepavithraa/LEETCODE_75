// LeetCode 994: Rotting Oranges
// You are given an m x n grid where each cell can have one of three values:
// 0 - an empty cell
// 1 - a fresh orange
// 2 - a rotten orange
// Every minute, any fresh orange that is 4-directionally adjacent to a rotten one becomes rotten.
// Return the minimum number of minutes that must elapse until no cell has a fresh orange.
// If this is impossible, return -1.

import java.util.*;

public class problem_48 {

    public int orangesRotting(int[][] grid) {
        int rows = grid.length;
        int cols = grid[0].length;
        Queue<int[]> queue = new LinkedList<>();
        int fresh = 0;
        int time = 0;

        // Step 1: Count fresh oranges and enqueue rotten ones
        for (int r = 0; r < rows; r++) {
            for (int c = 0; c < cols; c++) {
                if (grid[r][c] == 1) {
                    fresh++;
                } else if (grid[r][c] == 2) {
                    queue.offer(new int[]{r, c});
                }
            }
        }

        // 4-directional movement: right, left, down, up
        int[][] directions = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};

        // Step 2: BFS to rot fresh oranges
        while (!queue.isEmpty() && fresh > 0) {
            int size = queue.size();
            for (int i = 0; i < size; i++) {
                int[] point = queue.poll();
                int r = point[0], c = point[1];

                for (int[] d : directions) {
                    int row = r + d[0];
                    int col = c + d[1];
                    if (row >= 0 && row < rows && col >= 0 && col < cols && grid[row][col] == 1) {
                        grid[row][col] = 2;
                        fresh--;
                        queue.offer(new int[]{row, col});
                    }
                }
            }
            time++;
        }

        return fresh == 0 ? time : -1;
    }

    // ✅ Sample test case
    public static void main(String[] args) {
        problem_48 solution = new problem_48();
        int[][] grid = {
            {2, 1, 1},
            {1, 1, 0},
            {0, 1, 1}
        };
        int result = solution.orangesRotting(grid);
        System.out.println("Minutes until all oranges rot: " + result);
    }
}

// 🔍 Time Complexity: O(m * n), where m = number of rows, n = number of columns
// 🔍 Space Complexity: O(m * n), for the queue in worst case
