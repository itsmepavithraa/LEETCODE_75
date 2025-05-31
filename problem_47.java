/*
Question:
1926. Nearest Exit from Entrance in Maze (Leetcode)

You are given an m x n matrix maze (2D array) with characters:
- '.' (an empty cell)
- '+' (a wall)

You are also given the entrance cell coordinates [row, col], which is guaranteed to be an empty cell.

You need to find the minimum number of steps to reach any exit from the entrance.
An exit is any empty cell at the border of the maze except the entrance itself.

You can move in four directions (up, down, left, right), and cannot go through walls.

If there is no way to reach an exit, return -1.

Example:
Input:
maze = {
  {'+', '+', '.', '+'},
  {'.', '.', '.', '+'},
  {'+', '+', '+', '.'}
};
entrance = [1, 2];

Output: 1
*/

import java.util.*;

public class problem_47 {

    public int nearestExit(char[][] maze, int[] entrance) {
        int m = maze.length;
        int n = maze[0].length;

        Queue<int[]> queue = new LinkedList<>();
        queue.offer(new int[]{entrance[0], entrance[1], 0});
        maze[entrance[0]][entrance[1]] = '+'; // mark as visited

        int[][] directions = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};

        while (!queue.isEmpty()) {
            int[] curr = queue.poll();
            int r = curr[0], c = curr[1], steps = curr[2];

            for (int[] dir : directions) {
                int i = r + dir[0];
                int j = c + dir[1];

                if (i >= 0 && i < m && j >= 0 && j < n && maze[i][j] == '.') {
                    if (i == 0 || j == 0 || i == m - 1 || j == n - 1) {
                        return steps + 1;
                    }
                    queue.offer(new int[]{i, j, steps + 1});
                    maze[i][j] = '+'; // mark as visited
                }
            }
        }

        return -1;
    }

    public static void main(String[] args) {
        char[][] maze = {
            {'+', '+', '.', '+'},
            {'.', '.', '.', '+'},
            {'+', '+', '+', '.'}
        };
        int[] entrance = {1, 2};

        problem_47 sol = new problem_47();
        int result = sol.nearestExit(maze, entrance);
        System.out.println("Nearest exit steps: " + result); // Output: 1
    }
}

/*
Time Complexity: O(m * n)
- Each cell is visited at most once.

Space Complexity: O(m * n)
- Queue can grow up to number of empty cells in the worst case.
*/
