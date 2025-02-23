'''
LeetCode Problem: Container With Most Water

Problem Statement:
You are given an array height of n non-negative integers where each element represents the height of a vertical line.
The width between two lines is the distance between their indices. Find two lines that form a container, such that the container holds the most water.

Return the maximum amount of water a container can store.

Example:
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49

Explanation:
The lines at index 1 and index 8 form the container with the maximum area: (8 - 1) * min(8, 7) = 49.

Time Complexity: O(n)
Space Complexity: O(1)
'''

# Python Solution (Optimal Approach: Two Pointers)
from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        max_water = 0

        # Use two pointers to find the max area
        while left < right:
            # Calculate the current area
            current_water = (right - left) * min(height[left], height[right])
            max_water = max(max_water, current_water)

            # Move the pointer with the smaller height
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_water

# Example usage
if __name__ == "__main__":
    height = [1,8,6,2,5,4,8,3,7]
    solution = Solution()
    print("Maximum water contained:", solution.maxArea(height))