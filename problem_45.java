// 🔁 LeetCode 75: Reorder Routes to Make All Paths Lead to the City Zero
// ✅ Solved using BFS and HashMap in Java
// 🕒 Time Complexity: O(n)
// 💾 Space Complexity: O(n)

import java.util.*;

public class problem_45 {
    public int minReorder(int n, int[][] connections) {
        Map<Integer, List<Integer>> neighbors = new HashMap<>();
        Set<String> connectionSet = new HashSet<>();

        for (int i = 0; i < n; i++) {
            neighbors.put(i, new ArrayList<>());
        }

        for (int[] conn : connections) {
            int from = conn[0], to = conn[1];
            neighbors.get(from).add(to);  // Forward
            neighbors.get(to).add(from);  // Backward
            connectionSet.add(from + "->" + to);  // Save original direction
        }

        Queue<Integer> queue = new LinkedList<>();
        Set<Integer> visited = new HashSet<>();
        int reverse = 0;

        queue.offer(0);
        visited.add(0);

        while (!queue.isEmpty()) {
            int city = queue.poll();
            for (int neighbor : neighbors.get(city)) {
                if (!visited.contains(neighbor)) {
                    visited.add(neighbor);
                    if (!connectionSet.contains(neighbor + "->" + city)) {
                        reverse++; // Need to reverse this edge
                    }
                    queue.offer(neighbor);
                }
            }
        }

        return reverse;
    }

    // 🚀 Example Test Case
    public static void main(String[] args) {
        problem_45 solution = new problem_45();
        int n = 6;
        int[][] connections = {
            {0, 1}, {1, 3}, {2, 3}, {4, 0}, {4, 5}
        };

        int result = solution.minReorder(n, connections);
        System.out.println("Minimum roads to reverse: " + result); // Output: 3
    }
}
