// 📘 Problem: Max Consecutive Ones III (LeetCode)
// 
// Given a binary array `nums` and an integer `k`, return the length of the longest 
// subarray with at most `k` zeros that you can flip to 1.
// 
// 🧠 Example:
// Input: nums = [1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1], k = 2
// Output: 6
// Explanation: Flip up to 2 zeros to get the longest subarray of consecutive 1s.

public class problem_16 {
    public int longestOnes(int[] nums, int k) {
        int max_w = 0;
        int num_zeros = 0;
        int l = 0;

        for (int r = 0; r < nums.length; r++) {
            if (nums[r] == 0) {
                num_zeros++;
            }

            while (num_zeros > k) {
                if (nums[l] == 0) {
                    num_zeros--;
                }
                l++;
            }

            int w = r - l + 1;
            max_w = Math.max(max_w, w);
        }
        
        return max_w;
    }

    // 🔧 Test the function
    public static void main(String[] args) {
        problem_16 solution = new problem_16();
        
        int[] nums = {1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1};
        int k = 2;
        
        int result = solution.longestOnes(nums, k);
        
        System.out.println("Longest consecutive ones (with at most " + k + " flips): " + result);
    }
}

// ⚡ Time Complexity: O(N)
// - We traverse the array once, so the time complexity is linear.
//
// 🛢️ Space Complexity: O(1)
// - Only a few pointers and counters are used, so the space complexity is constant.
