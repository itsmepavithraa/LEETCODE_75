# LeetCode Problem: Equal Row and Column Pairs
# 
# **Problem Statement:**
# Given an `n x n` matrix `grid`, return the number of pairs `(ri, ci)` such that row `ri` and column `ci` are equal.
# 
# **Example:**
# ```
# Input: grid = [[3,2,1],[1,7,6],[2,7,7]]
# Output: 1
# Explanation: There is 1 pair where row and column are equal:
# - (0, 2): Row 0 -> [3, 2, 1], Column 2 -> [3, 2, 1]
# ```
#
# **Constraints:**
# - `n == grid.length`
# - `n == grid[i].length`
# - `1 <= n <= 200`
# - `1 <= grid[i][j] <= 10^5`

from collections import defaultdict
from typing import List

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        row_count = defaultdict(int)
        count = 0
        
        # Count the frequency of each row
        for row in grid:
            row_count[tuple(row)] += 1
        
        # Count matching columns
        for column in zip(*grid):
            count += row_count[column]
        
        return count

# Time Complexity: O(n^2)
# - We traverse all rows and columns, which takes O(n^2).
# - Dictionary operations (insertion and lookup) take O(1) on average.

# Space Complexity: O(n^2)
# - We store up to `n` rows in the dictionary, each of length `n`.

# Example usage:
if __name__ == "__main__":
    sol = Solution()
    grid = [[3,2,1],[1,7,6],[2,7,7]]
    result = sol.equalPairs(grid)
    print("Number of equal row and column pairs:", result)

# Output: Number of equal row and column pairs: 1
