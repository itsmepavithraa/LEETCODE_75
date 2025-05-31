"""
Question:
1926. Nearest Exit from Entrance in Maze (Leetcode)

You are given an `m x n` matrix `maze` (2D list) with characters:
- '.' (an empty cell)
- '+' (a wall)

You are also given the `entrance` cell coordinates [row, col], which is guaranteed to be an empty cell.

You need to find the **minimum number of steps** to reach **any exit** from the entrance. An exit is any empty cell **at the border of the maze** **except** the entrance itself.

You can only move in four cardinal directions (up, down, left, right), and you cannot go through walls.

If there is no way to reach an exit, return -1.

Example:
Input:
maze = [["+","+",".","+"],
        [".",".",".","+"],
        ["+","+","+","."]]
entrance = [1,2]

Output: 1
Explanation: The nearest exit is at [0,2], which is 1 step away from the entrance.
"""

from collections import deque
from typing import List

class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        cells = deque([(entrance[0], entrance[1], 0)])
        maze[entrance[0]][entrance[1]] = "+"  # Mark entrance as visited
        rows, cols = len(maze), len(maze[0])
        
        while cells:
            r, c, steps = cells.popleft()
            checks = [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]
            for i, j in checks:
                if 0 <= i < rows and 0 <= j < cols and maze[i][j] == ".":
                    if i == 0 or j == 0 or i == rows - 1 or j == cols - 1:
                        return steps + 1
                    cells.append((i, j, steps + 1))
                    maze[i][j] = "+"  # Mark visited
        return -1

# Example test case
maze = [["+","+",".","+"],
        [".",".",".","+"],
        ["+","+","+","."]]
entrance = [1,2]

sol = Solution()
print(sol.nearestExit(maze, entrance))  # Output: 1

"""
Time Complexity: O(m * n)
- Each cell is visited at most once.

Space Complexity: O(m * n)
- In worst case, the queue stores all empty cells.
"""
