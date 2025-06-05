// LeetCode 2462: Total Cost to Hire K Workers

// Problem:
// You are given a 0-indexed integer array costs where costs[i] is the cost of hiring the i-th worker.
// You are also given two integers k and candidates.
// You want to hire exactly k workers from either the beginning or the end of the costs list.
// To do this, you will run the following steps exactly k times:
//
// - In each step, choose candidates workers from the beginning of the list who have not been hired.
// - Choose candidates workers from the end of the list who have not been hired.
// - Among the selected workers, pick the one with the lowest cost.
//   - If there is a tie, choose the worker with the smaller index.
// - Remove the chosen worker from the list (so they cannot be chosen again).
//
// Return the total cost to hire exactly k workers.

// Time Complexity: O(k * log(candidates))
// Space Complexity: O(candidates)

import java.util.*;

public class problem_52 {
    public int totalCost(int[] costs, int k, int candidates) {
        int n = costs.length;
        int i = 0, j = n - 1;
        PriorityQueue<Integer> left = new PriorityQueue<>();
        PriorityQueue<Integer> right = new PriorityQueue<>();
        int total = 0;

        while (k > 0) {
            while (left.size() < candidates && i <= j) {
                left.offer(costs[i++]);
            }

            while (right.size() < candidates && j >= i) {
                right.offer(costs[j--]);
            }

            if (right.isEmpty() || (!left.isEmpty() && left.peek() <= right.peek())) {
                total += left.poll();
            } else {
                total += right.poll();
            }

            k--;
        }

        return total;
    }

    // Example usage
    public static void main(String[] args) {
        problem_52 obj = new problem_52();
        int[] costs = {17, 12, 10, 2, 7, 2, 11, 20, 8};
        int k = 3;
        int candidates = 4;
        int result = obj.totalCost(costs, k, candidates);
        System.out.println(result); // Output: 11
    }
}
