/*
LeetCode 547. Number of Provinces

🧠 Problem Statement:
There are n cities. Some of them are connected directly, some indirectly, and some not at all.  
A province is a group of directly or indirectly connected cities, and no other cities outside of the group.  

You are given an n x n matrix isConnected where isConnected[i][j] = 1  
if the ith city and the jth city are directly connected, and 0 otherwise.  

Return the total number of provinces.

🔗 Link: https://leetcode.com/problems/number-of-provinces/
*/

public class problem44 {

    public int findCircleNum(int[][] isConnected) {
        int n = isConnected.length;
        boolean[] visited = new boolean[n];
        int provinces = 0;

        for (int city = 0; city < n; city++) {
            if (!visited[city]) {
                dfs(isConnected, visited, city);
                provinces++;
            }
        }

        return provinces;
    }

    private void dfs(int[][] isConnected, boolean[] visited, int city) {
        visited[city] = true;
        for (int otherCity = 0; otherCity < isConnected.length; otherCity++) {
            if (isConnected[city][otherCity] == 1 && !visited[otherCity]) {
                dfs(isConnected, visited, otherCity);
            }
        }
    }

    // ------------------------------
    // 🚀 Example Test Case
    public static void main(String[] args) {
        problem44 solution = new problem44();
        int[][] isConnected = {
            {1, 1, 0},
            {1, 1, 0},
            {0, 0, 1}
        };
        int result = solution.findCircleNum(isConnected);
        System.out.println("Number of Provinces: " + result); // Output: 2
    }
}

/*
📊 Time and Space Complexity:
Time Complexity: O(n^2) — We visit each connection once.
Space Complexity: O(n) — For the visited array and recursion stack.
*/

