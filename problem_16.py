# 📘 Problem: Max Consecutive Ones III (LeetCode)
# 
# Given a binary array `nums` and an integer `k`, return the length of the longest 
# subarray with at most `k` zeros that you can flip to 1.
# 
# 🧠 Example:
# Input: nums = [1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1], k = 2
# Output: 6
# Explanation: Flip up to 2 zeros to get the longest subarray of consecutive 1s.

from typing import List

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        max_w = 0
        num_zeros = 0
        n = len(nums)
        l = 0
        
        for r in range(n):
            if nums[r] == 0:
                num_zeros += 1
            
            while num_zeros > k:
                if nums[l] == 0:
                    num_zeros -= 1
                l += 1

            w = r - l + 1
            max_w = max(max_w, w)
        
        return max_w

# 🔧 Test the function
if __name__ == "__main__":
    nums = [1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1]
    k = 2
    solution = Solution()
    result = solution.longestOnes(nums, k)
    print(f"Longest consecutive ones (with at most {k} flips): {result}")

# ⚡ Time Complexity: O(N)
# - We traverse the array once, so the time complexity is linear.
# 
# 🛢️ Space Complexity: O(1)
# - Only a few pointers and counters are used, so the space complexity is constant.
