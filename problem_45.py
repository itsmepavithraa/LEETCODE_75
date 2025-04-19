# 🔁 LeetCode 75: Reorder Routes to Make All Paths Lead to the City Zero
# ✅ Solved using BFS and defaultdict in Python
# 🕒 Time Complexity: O(n)
# 💾 Space Complexity: O(n)

from collections import defaultdict
from typing import List

class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        neighbors = defaultdict(list)  # List that stores all the connected cities
        connection = set()  # Track of original direction (from -> to)

        for start, end in connections:
            neighbors[start].append(end)  # Forward direction
            neighbors[end].append(start)  # Backward direction
            connection.add((start, end))  # Save the original directed edge

        curr = [0]  # Start BFS from city 0 (capital city)
        reverse = 0  # Counts roads to reverse toward city 0
        visited = set()  # To avoid revisiting the same cities
        visited.add(0)  # Mark city 0 as visited

        while curr:
            new_curr = []  # List of cities to visit next
            for city in curr:
                for n in neighbors[city]:
                    if n not in visited:
                        visited.add(n)
                        if (n, city) not in connection:  # Edge not in correct direction
                            reverse += 1
                        new_curr.append(n)
            curr = new_curr  # Move to the next level of BFS

        return reverse

# 🚀 Example Test Case:
# n = 6, connections = [[0,1],[1,3],[2,3],[4,0],[4,5]]
# Expected Output: 3

solution = Solution()
n = 6
connections = [[0,1],[1,3],[2,3],[4,0],[4,5]]
print("Minimum roads to reverse:", solution.minReorder(n, connections))
