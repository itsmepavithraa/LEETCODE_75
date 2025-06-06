/*
🧠 Problem: Kth Largest Element in an Array (LeetCode 215)

Given an integer array nums and an integer k, return the kth largest element in the array.
Note that it is the kth largest element in the sorted order, not the kth distinct element.

Example 1:
Input: nums = [3,2,1,5,6,4], k = 2
Output: 5

Example 2:
Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4

⏱ Time Complexity: O(n log n) – due to sorting
📦 Space Complexity: O(1) – in-place sorting
*/

import java.util.Arrays;

public class problem_49 {

    public int findKthLargest(int[] nums, int k) {
        Arrays.sort(nums); // Sort the array
        return nums[nums.length - k]; // Return the kth largest
    }

    public static void main(String[] args) {
        problem_49 solution = new problem_49();

        // Test Case 1
        int[] nums1 = {3, 2, 1, 5, 6, 4};
        int k1 = 2;
        System.out.println("Output: " + solution.findKthLargest(nums1, k1)); // Output: 5

        // Test Case 2
        int[] nums2 = {3, 2, 3, 1, 2, 4, 5, 5, 6};
        int k2 = 4;
        System.out.println("Output: " + solution.findKthLargest(nums2, k2)); // Output: 4
    }
}
