"""
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
"""

def findMaxAverage(nums, k):
    # Step 1: Calculate the initial window sum
    window_sum = sum(nums[:k])
    max_sum = window_sum

    # Step 2: Slide the window through the array
    for i in range(k, len(nums)):
        # Add the next element, remove the first element of the previous window
        window_sum += nums[i] - nums[i - k]
        # Update the maximum sum
        max_sum = max(max_sum, window_sum)

    # Step 3: Return the maximum average
    return max_sum / k

# Example usage
nums = [1, 12, -5, -6, 50, 3]
k = 4
result = findMaxAverage(nums, k)
print(f"Maximum average subarray of size {k}: {result}")

"""
Time Complexity: O(N)
- We traverse the array exactly once, sliding the window.

Space Complexity: O(1)
- Constant space, only a few variables are used.
"""
