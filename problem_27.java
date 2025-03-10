// Number of Recent Calls Problem

// Problem Statement:
// Design a class RecentCounter that counts recent requests within a sliding window of 3000 milliseconds.
// 
// Implement the following methods:
// - RecentCounter(): Initializes the counter.
// - ping(int t): Adds a new request at time t, and returns the number of requests 
//                that occurred in the time range [t - 3000, t], inclusive.
//
// Example:
// Input: ["RecentCounter", "ping", "ping", "ping", "ping"]
//        [[], [1], [100], [3001], [3002]]
// Output: [null, 1, 2, 3, 3]
//
// Explanation:
// ping(1) → 1 request in the last 3000 ms
// ping(100) → 2 requests in the last 3000 ms
// ping(3001) → 3 requests in the last 3000 ms
// ping(3002) → 3 requests in the last 3000 ms (request at 1 is removed)

import java.util.LinkedList;
import java.util.Queue;

public class problem_27 {
    private Queue<Integer> q;

    public problem_27() {
        q = new LinkedList<>();
    }

    public int ping(int t) {
        // Add the current timestamp to the queue
        q.add(t);
        
        // Remove timestamps older than 3000 milliseconds
        while (!q.isEmpty() && q.peek() < t - 3000) {
            q.poll();
        }
        
        // Return the count of recent requests
        return q.size();
    }

    // Example usage
    public static void main(String[] args) {
        problem_27 obj = new problem_27();
        System.out.println(obj.ping(1));    // Output: 1
        System.out.println(obj.ping(100));  // Output: 2
        System.out.println(obj.ping(3001)); // Output: 3
        System.out.println(obj.ping(3002)); // Output: 3
    }
}

// Time Complexity: O(1) (amortized)
// Space Complexity: O
