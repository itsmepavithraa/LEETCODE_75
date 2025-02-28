// Problem: Longest Subarray of 1's After Deleting One Element
//
// Given a binary array nums, you should delete one element from it.
// Return the size of the longest non-empty subarray containing only 1's in the resulting array.
//
// Example 1:
// Input: nums = [1,1,0,1,1,1]
// Output: 5
// Explanation: Delete the 0 in the middle to get [1,1,1,1,1], which length is 5.
//
// Example 2:
// Input: nums = [0,1,1,1,0,1,1,0,1]
// Output: 4
// Explanation: Delete one 0 to get the longest subarray of 1s.
//
// Constraints:
// - 1 <= nums.length <= 10^5
// - nums[i] is either 0 or 1.

public class problem_17 {

    public int longestSubarray(int[] nums) {
        int maxLen = 0;
        int start = 0;
        int zeroIndex = -1;

        for (int i = 0; i < nums.length; i++) {
            if (nums[i] == 0) {
                start = zeroIndex + 1;
                zeroIndex = i;
            }
            maxLen = Math.max(maxLen, i - start);
        }

        return maxLen;
    }

    public static void main(String[] args) {
        problem_17 solution = new problem_17();
        
        int[] nums1 = {1, 1, 0, 1, 1, 1};
        System.out.println("Longest Subarray Length 1: " + solution.longestSubarray(nums1));  // Output: 5
        
        int[] nums2 = {0, 1, 1, 1, 0, 1, 1, 0, 1};
        System.out.println("Longest Subarray Length 2: " + solution.longestSubarray(nums2));  // Output: 4
    }
}

// Time Complexity: O(N)
// - We traverse the array once, so the time complexity is linear.
//
// Space Complexity: O(1)
// - We only use a few extra variables, so the space complexity is constant.
