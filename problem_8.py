"""
Problem: Increasing Triplet Subsequence

Given an integer array nums, return True if there exists a strictly increasing 
subsequence of length 3. Otherwise, return False.

Example 1:
Input: nums = [1, 2, 3, 4, 5]
Output: True

Example 2:
Input: nums = [5, 4, 3, 2, 1]
Output: False

Example 3:
Input: nums = [2, 1, 5, 0, 4, 6]
Output: True

Constraints:
- 1 <= nums.length <= 10^5
- -2^31 <= nums[i] <= 2^31 - 1

Time Complexity: O(n)  -> We traverse the list once.
Space Complexity: O(1) -> We use only two variables.
"""

def increasingTriplet(nums):
    first = float('inf')
    second = float('inf')

    for num in nums:
        if num <= first:
            first = num  # Smallest element
        elif num <= second:
            second = num  # Second smallest element
        else:
            return True  # Found a triplet (first < second < num)
    
    return False

# Example Usage
if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5]
    print("Input:", nums)
    print("Output:", increasingTriplet(nums))  # Output: True

    nums = [5, 4, 3, 2, 1]
    print("Input:", nums)
    print("Output:", increasingTriplet(nums))  # Output: False

    nums = [2, 1, 5, 0, 4, 6]
    print("Input:", nums)
    print("Output:", increasingTriplet(nums))  # Output: True
