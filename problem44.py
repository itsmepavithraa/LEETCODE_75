from typing import List

"""
LeetCode 547. Number of Provinces

🧠 Problem Statement:
There are n cities. Some of them are connected directly, some indirectly, and some not at all.  
A province is a group of directly or indirectly connected cities, and no other cities outside of the group.  

You are given an n x n matrix isConnected where isConnected[i][j] = 1  
if the ith city and the jth city are directly connected, and 0 otherwise.  

Return the total number of provinces.

🔗 Link: https://leetcode.com/problems/number-of-provinces/
"""

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def dfs(city):
            visited[city] = True
            for other_city in range(len(isConnected)):
                if isConnected[city][other_city] == 1 and not visited[other_city]:
                    dfs(other_city)

        n = len(isConnected)
        visited = [False] * n
        provinces = 0

        for city in range(n):
            if not visited[city]:
                dfs(city)
                provinces += 1

        return provinces

# ------------------------------
# 🚀 Example Test Case
if __name__ == "__main__":
    isConnected = [
        [1, 1, 0],
        [1, 1, 0],
        [0, 0, 1]
    ]
    sol = Solution()
    print("Number of Provinces:", sol.findCircleNum(isConnected))  # Output: 2

# ------------------------------
# 📊 Time and Space Complexity:
# Time Complexity: O(n^2) — We check each pair of cities once.
# Space Complexity: O(n) — Visited array and recursion stack for DFS.
