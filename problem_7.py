"""
Problem: Product of Array Except Self

Given an integer array nums, return an array answer such that answer[i] is the product of all the elements of nums except nums[i].

Constraints:
- Solve it **without using division** and in **O(n) time complexity**.

Time Complexity: O(n) - We traverse the array twice (once for prefix and once for suffix product computation).
Space Complexity: O(1) - Output array is not considered extra space as per problem constraints.
"""
from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [1] * n  # Output array initialized with 1s
    
        # Compute prefix product
        prefix = 1
        for i in range(n):
            result[i] = prefix  # Store prefix product before multiplying with nums[i]
            prefix *= nums[i]    # Update prefix for next iteration
    
        # Compute suffix product and multiply with prefix values
        suffix = 1
        for i in range(n - 1, -1, -1):
            result[i] *= suffix  # Multiply suffix product to existing value in result
            suffix *= nums[i]     # Update suffix for next iteration

        return result

# Example usage
test_case = [1, 2, 3, 4]
solution = Solution()
print(solution.productExceptSelf(test_case))  # Output: [24, 12, 8, 6]
