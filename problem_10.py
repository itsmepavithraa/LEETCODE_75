# LeetCode Problem 283: Move Zeroes
# Solution using List Partitioning Approach

from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Moves all 0's to the end of the array while maintaining the relative order of non-zero elements.
        This is done in-place without making a copy of the array.
        """
        zero = []  # Stores all zeroes
        non_zero = []  # Stores all non-zero elements
        
        for num in nums:
            if num == 0:
                zero.append(num)
            else:
                non_zero.append(num)
        
        nums.clear()  # Clear the original list
        nums.extend(non_zero + zero)  # Concatenate non-zero elements followed by zeroes

# Example Usage
nums = [0, 1, 0, 3, 12]
sol = Solution()
sol.moveZeroes(nums)
print(nums)  # Output: [1, 3, 12, 0, 0]

# Time Complexity: O(n) - We iterate through the array once.
# Space Complexity: O(n) - Extra space is used to store non-zero and zero elements separately.
