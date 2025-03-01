// LeetCode Problem: Find the Highest Altitude

// 🚩 Problem Statement:
// You are given an array `gain` of length `n` where `gain[i]` is the net gain in altitude between points `i` and `i + 1`.
// The altitude starts at 0. Return the highest altitude.

// 🧠 Example:
// Input: gain = [-5, 1, 5, 0, -7]
// Output: 1
// Explanation:
// Altitude changes: [0, -5, -4, 1, 1, -6]
// The highest altitude is 1.

public class problem_18 {
    public int largestAltitude(int[] gain) {
        int altitude = 0;
        int maxAltitude = 0;

        for (int change : gain) {
            altitude += change;
            maxAltitude = Math.max(maxAltitude, altitude);
        }

        return maxAltitude;
    }

    // 🔧 Test the solution:
    public static void main(String[] args) {
        problem_18 solution = new problem_18();
        
        int[] gain = {-5, 1, 5, 0, -7};
        System.out.println("Highest Altitude: " + solution.largestAltitude(gain));
    }
}

// 🕒 Time Complexity: O(n)
// We traverse the `gain` array once, so the time complexity is linear.

// 🛢 Space Complexity: O(1)
// We use only a few variables, so the space complexity is constant.