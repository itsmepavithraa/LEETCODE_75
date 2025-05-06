"""
Problem: Evaluate Division

You are given an array of equations `equations` where each equation is a list of two variables [A, B],
and an array `values` where `values[i]` represents the result of the equation A / B = values[i].
You are also given some `queries`, where each query is a list of two variables [C, D].
Return the answers to each query. If the answer does not exist, return -1.0.

Example:
Input:
equations = [["a","b"],["b","c"]]
values = [2.0,3.0]
queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]

Output: [6.0,0.5,-1.0,1.0,-1.0]
"""

import collections
from typing import List

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # STEP 1: BUILD THE GRAPH
        graph = collections.defaultdict(dict)
        for (x, y), val in zip(equations, values):
            graph[x][y] = val
            graph[y][x] = 1.0 / val

        # STEP 2: DFS FUNCTION
        def dfs(x, y, visited):
            if x not in graph or y not in graph:
                return -1.0
            if y in graph[x]:
                return graph[x][y]
            for nei in graph[x]:
                if nei not in visited:
                    visited.add(nei)
                    temp = dfs(nei, y, visited)
                    if temp != -1:
                        return graph[x][nei] * temp
            return -1.0

        # STEP 3: PROCESS EACH QUERY
        res = []
        for query in queries:
            res.append(dfs(query[0], query[1], set([query[0]])))
        return res


# Example usage
if __name__ == "__main__":
    equations = [["a", "b"], ["b", "c"]]
    values = [2.0, 3.0]
    queries = [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]
    sol = Solution()
    print(sol.calcEquation(equations, values, queries))
