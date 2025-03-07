// LeetCode Problem: Removing Stars From a String
// 
// **Problem Statement:**
// You are given a string `s`, which contains stars `*`.
// In one operation, you can:
// - Choose a star in `s`.
// - Remove the closest non-star character to its left, along with the star itself.
// Return the string after all stars have been removed.
//
// **Example:**
// ```
// Input: s = "leet**cod*e"
// Output: "lecoe"
// Explanation: Performing the removals:
// - The first star removes the 't'.
// - The second star removes the 'e'.
// - The third star removes the 'd'.
// ```
// 
// **Constraints:**
// - `1 <= s.length <= 10^5`
// - `s` consists of lowercase English letters and stars `*`.

public class problem_24 {
    public String removeStars(String s) {
        StringBuilder stack = new StringBuilder();
        
        // Process each character
        for (char c : s.toCharArray()) {
            if (c == '*') {
                if (stack.length() > 0) {
                    stack.deleteCharAt(stack.length() - 1);  // Remove the last character
                }
            } else {
                stack.append(c);
            }
        }
        
        return stack.toString();
    }

    // Time Complexity: O(n)
    // - We traverse the string once, and each character is added or removed at most once.

    // Space Complexity: O(n)
    // - The stack (StringBuilder) stores characters that are not removed.

    // Example usage:
    public static void main(String[] args) {
        problem_24 sol = new problem_24();
        String s = "leet**cod*e";
        String result = sol.removeStars(s);
        System.out.println("Resulting string after removing stars: " + result);
    }
}

// Output: Resulting string after removing stars: lecoe


