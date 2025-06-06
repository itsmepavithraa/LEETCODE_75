"""
🧠 Problem: Kth Largest Element in an Array (LeetCode 215)

Given an integer array nums and an integer k, return the kth largest element in the array.
Note that it is the kth largest element in the sorted order, not the kth distinct element.

Example 1:
Input: nums = [3,2,1,5,6,4], k = 2
Output: 5

Example 2:
Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4

⏱ Time Complexity: O(n log n), where n is the length of the array (for sorting)
📦 Space Complexity: O(1) – in-place sorting
"""

from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort()
        return nums[len(nums) - k]

# Example usage
if __name__ == "__main__":
    sol = Solution()
    # Test Case 1
    print("Output:", sol.findKthLargest([3, 2, 1, 5, 6, 4], 2))  # Output: 5
    # Test Case 2
    print("Output:", sol.findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4))  # Output: 4
