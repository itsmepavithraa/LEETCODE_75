/**
 * LeetCode Problem 1679: Max Number of K-Sum Pairs
 * Difficulty: Medium
 * 
 * Problem Statement:
 * You are given an integer array `nums` and an integer `k`.
 * 
 * In one operation, you can pick two numbers from the array whose sum equals `k` and remove them from the array.
 * 
 * Return the maximum number of operations you can perform.
 * 
 * Example 1:
 * Input: nums = [1, 2, 3, 4], k = 5
 * Output: 2
 * Explanation: The pairs (1, 4) and (2, 3) sum up to 5.
 * 
 * Example 2:
 * Input: nums = [3, 1, 3, 4, 3], k = 6
 * Output: 1
 * Explanation: The only pair that sums up to 6 is (3, 3).
 * 
 * Constraints:
 * 1 <= nums.length <= 10^5
 * 1 <= nums[i] <= 10^9
 * 1 <= k <= 10^9
 * 
 * Approach:
 * 1. Sort the array.
 * 2. Use two pointers (`left` and `right`).
 * 3. Move pointers inward based on the sum of elements:
 *    - If the sum equals `k`, count a pair and move both pointers.
 *    - If the sum is less than `k`, move the `left` pointer right.
 *    - If the sum is greater than `k`, move the `right` pointer left.
 * 4. Return the total number of valid pairs formed.
 * 
 * Time Complexity: O(N log N) - Due to sorting.
 * Space Complexity: O(1) - Constant space.
 */

import java.util.Arrays;

public class problem_13 {
    public int maxOperations(int[] nums, int k) {
        Arrays.sort(nums);
        int left = 0, right = nums.length - 1;
        int count = 0;
        
        while (left < right) {
            int currentSum = nums[left] + nums[right];
            
            if (currentSum == k) {
                count++;
                left++;
                right--;
            } else if (currentSum < k) {
                left++;
            } else {
                right--;
            }
        }
        
        return count;
    }

    // Example usage
    public static void main(String[] args) {
        problem_13 solution = new problem_13();
        int[] nums = {1, 2, 3, 4};
        int k = 5;
        System.out.println(solution.maxOperations(nums, k)); // Output: 2
    }
}
    

