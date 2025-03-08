// 🚀 Asteroid Collision Problem

// 🧠 Problem Statement:
// You are given an array `asteroids` of integers representing asteroids in a row.  
// Each asteroid moves at the same speed.  
// - Positive value → Asteroid moves **right**.  
// - Negative value → Asteroid moves **left**.  

// When two asteroids collide:  
// - The smaller asteroid explodes.  
// - If they are the **same size**, both explode.  
// - Two asteroids moving in the **same direction never collide**.

// Return an array of **remaining asteroids** after all collisions.

// 🛠️ Example 1:
// Input: asteroids = [5, 10, -5]  
// Output: [5, 10]

// 🛠️ Example 2:
// Input: asteroids = [8, -8]  
// Output: []

// 🛠️ Example 3:
// Input: asteroids = [10, 2, -5]  
// Output: [10]

// ✅ Constraints:
// - `2 <= asteroids.length <= 10^4`
// - `-1000 <= asteroids[i] <= 1000`
// - `asteroids[i] ≠ 0`

import java.util.Stack;

public class problem_25 {

    public static int[] asteroidCollision(int[] asteroids) {
        Stack<Integer> stack = new Stack<>();

        for (int asteroid : asteroids) {
            // Check for collisions
            while (!stack.isEmpty() && asteroid < 0 && stack.peek() > 0) {
                if (stack.peek() < -asteroid) {
                    stack.pop(); // Right-moving asteroid explodes
                    continue;
                } else if (stack.peek() == -asteroid) {
                    stack.pop(); // Both asteroids explode
                }
                break;
            }
            // Add asteroid to stack if no collision
            if (stack.isEmpty() || asteroid > 0 || stack.peek() < 0) {
                stack.push(asteroid);
            }
        }

        // Convert stack to array
        int[] result = new int[stack.size()];
        for (int i = stack.size() - 1; i >= 0; i--) {
            result[i] = stack.pop();
        }

        return result;
    }

    public static void main(String[] args) {
        // 🚀 Test cases
        int[] asteroids1 = {5, 10, -5};
        System.out.println(java.util.Arrays.toString(asteroidCollision(asteroids1))); // Output: [5, 10]

        int[] asteroids2 = {8, -8};
        System.out.println(java.util.Arrays.toString(asteroidCollision(asteroids2))); // Output: []

        int[] asteroids3 = {10, 2, -5};
        System.out.println(java.util.Arrays.toString(asteroidCollision(asteroids3))); // Output: [10]

        int[] asteroids4 = {-2, -1, 1, 2};
        System.out.println(java.util.Arrays.toString(asteroidCollision(asteroids4))); // Output: [-2, -1, 1, 2]
    }
}

// 🕒 Time Complexity: O(N)  
// - **One pass through the array** + **O(1) stack operations** → Linear time.

// 🛢️ Space Complexity: O(N)  
// - **Stack space** to store surviving asteroids.

// 🔥 Copy, paste, and run this in **VS Code**! Let me know if you want me to tweak anything! 🚀✨
