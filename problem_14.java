/*
LeetCode 643: Maximum Average Subarray I

Problem Statement:
Given an array `nums` consisting of `n` integers, and an integer `k`, 
find the contiguous subarray of length `k` that has the maximum average value 
and return this value.

Example:
Input: nums = [1, 12, -5, -6, 50, 3], k = 4
Output: 12.75

Explanation:
- Subarray [12, -5, -6, 50] has the maximum sum = 51
- Maximum average = 51 / 4 = 12.75
*/

public class problem_14 {
    public static double findMaxAverage(int[] nums, int k) {
        // Step 1: Calculate the initial window sum
        int windowSum = 0;
        for (int i = 0; i < k; i++) {
            windowSum += nums[i];
        }
        int maxSum = windowSum;

        // Step 2: Slide the window through the array
        for (int i = k; i < nums.length; i++) {
            // Add the next element, remove the first element of the previous window
            windowSum += nums[i] - nums[i - k];
            // Update the maximum sum
            maxSum = Math.max(maxSum, windowSum);
        }

        // Step 3: Return the maximum average
        return (double) maxSum / k;
    }

    public static void main(String[] args) {
        // Example usage
        int[] nums = {1, 12, -5, -6, 50, 3};
        int k = 4;
        double result = findMaxAverage(nums, k);
        System.out.println("Maximum average subarray of size " + k + ": " + result);
    }
}

/*
Time Complexity: O(N)
- We traverse the array exactly once, sliding the window.

Space Complexity: O(1)
- Constant space, only a few variables are used.
*/
