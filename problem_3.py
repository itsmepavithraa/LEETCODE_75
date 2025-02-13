"""
LeetCode 1431: Kids With the Greatest Number of Candies

Problem:
- Given a list `candies` where each element represents the candies a kid has.
- You can give `extraCandies` to any kid.
- Return a list of booleans where `True` means the kid can have the most candies.

Example:
---------
Input:  candies = [2,3,5,1,3], extraCandies = 3
Output: [True, True, True, False, True]

Constraints:
------------
- 2 <= len(candies) <= 100
- 1 <= candies[i] <= 100
- 1 <= extraCandies <= 50
"""

from typing import List

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candy = max(candies)  # Find the maximum candy count
        result = []
        
        for candy in candies:
            result.append(candy + extraCandies >= max_candy)  # Check if it becomes the max
        
        return result

# Example Usage
if __name__ == "__main__":
    solution = Solution()
    candies = [2, 3, 5, 1, 3]
    extraCandies = 3
    print(solution.kidsWithCandies(candies, extraCandies))  # Output: [True, True, True, False, True]

# Time Complexity: O(n)
# Space Complexity: O(n)
