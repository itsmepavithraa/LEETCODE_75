/*
LeetCode Problem: Container With Most Water

Problem Statement:
You are given an array height of n non-negative integers where each element represents the height of a vertical line.
The width between two lines is the distance between their indices. Find two lines that form a container, such that the container holds the most water.

Return the maximum amount of water a container can store.

Example:
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49

Explanation:
The lines at index 1 and index 8 form the container with the maximum area: (8 - 1) * min(8, 7) = 49.

Time Complexity: O(n)
Space Complexity: O(1)
*/

public class problem_12 {
    
    // Java Solution (Optimal Approach: Two Pointers)
    public int maxArea(int[] height) {
        int left = 0;
        int right = height.length - 1;
        int maxWater = 0;

        // Use two pointers to find the max area
        while (left < right) {
            // Calculate the current area
            int currentWater = (right - left) * Math.min(height[left], height[right]);
            maxWater = Math.max(maxWater, currentWater);

            // Move the pointer with the smaller height
            if (height[left] < height[right]) {
                left++;
            } else {
                right--;
            }
        }
        return maxWater;
    }

    // Example usage
    public static void main(String[] args) {
        problem_12 solution = new problem_12();
        int[] height = {1, 8, 6, 2, 5, 4, 8, 3, 7};
        System.out.println("Maximum water contained (Java): " + solution.maxArea(height));
    }
}

/*
Time Complexity: O(n)
Space Complexity: O(1)
*/
