# Problem: Longest Subarray of 1's After Deleting One Element
# 
# Given a binary array nums, you should delete one element from it.
# Return the size of the longest non-empty subarray containing only 1's in the resulting array.
# 
# Example 1:
# Input: nums = [1,1,0,1,1,1]
# Output: 5
# Explanation: Delete the 0 in the middle to get [1,1,1,1,1], which length is 5.
# 
# Example 2:
# Input: nums = [0,1,1,1,0,1,1,0,1]
# Output: 4
# Explanation: Delete one 0 to get the longest subarray of 1s.
# 
# Constraints:
# - 1 <= nums.length <= 10^5
# - nums[i] is either 0 or 1.

from typing import List

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        max_len = 0
        start = 0
        zero = -1
        
        for i in range(len(nums)):
            if nums[i] == 0:
                start = zero + 1
                zero = i
            max_len = max(max_len, i - start)
        
        return max_len

# Time Complexity: O(N)  
# - We traverse the array once, so the time complexity is linear.
# 
# Space Complexity: O(1)  
# - We only use a few extra variables, so the space complexity is constant.

# Example usage
if __name__ == "__main__":
    solution = Solution()
    nums = [1, 1, 0, 1, 1, 1]
    print("Longest Subarray Length:", solution.longestSubarray(nums))  # Output: 5
