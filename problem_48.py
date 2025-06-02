# LeetCode 994: Rotting Oranges
# You are given an m x n grid where each cell can have one of three values:
# 0 - an empty cell
# 1 - a fresh orange
# 2 - a rotten orange
# Every minute, any fresh orange that is 4-directionally adjacent to a rotten one becomes rotten.
# Return the minimum number of minutes that must elapse until no cell has a fresh orange.
# If this is impossible, return -1.

from collections import deque
from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        time, fresh = 0, 0
        rows, cols = len(grid), len(grid[0])

        # Step 1: Count fresh oranges and enqueue rotten oranges
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    q.append((r, c))

        # 4-directional movement: right, left, down, up
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        # Step 2: BFS to rot fresh oranges
        while q and fresh > 0:
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    row, col = r + dr, c + dc
                    if 0 <= row < rows and 0 <= col < cols and grid[row][col] == 1:
                        grid[row][col] = 2       # Rot the orange
                        fresh -= 1               # Decrease fresh count
                        q.append((row, col))     # Add newly rotten to queue
            time += 1

        return time if fresh == 0 else -1


# ✅ Sample test case
if __name__ == "__main__":
    grid = [
        [2, 1, 1],
        [1, 1, 0],
        [0, 1, 1]
    ]
    solution = Solution()
    result = solution.orangesRotting(grid)
    print("Minutes until all oranges rot:", result)

# 🔍 Time Complexity: O(m * n), where m = number of rows, n = number of columns
# 🔍 Space Complexity: O(m * n), for the queue in worst case
