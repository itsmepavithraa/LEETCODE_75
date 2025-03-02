
# LeetCode 75: Find Pivot Index (Python Solution)

"""
🧠 Problem Statement:
Given an array of integers `nums`, find the pivot index.  
The pivot index is the index where the sum of all elements to the left is equal to the sum of all elements to the right.  

Return the leftmost pivot index. If no such index exists, return -1.

🔑 Example:
Input: nums = [1, 7, 3, 6, 5, 6]  
Output: 3  
Explanation:  
- Left sum: 1 + 7 + 3 = 11  
- Right sum: 5 + 6 = 11  

📘 Constraints:  
- 1 <= nums.length <= 10^4  
- -1000 <= nums[i] <= 1000  
"""

from typing import List

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left_sum = 0
        right_sum = sum(nums)
        
        for i in range(len(nums)):
            right_sum -= nums[i]
            if left_sum == right_sum:
                return i
            left_sum += nums[i]
        
        return -1

# 🛠️ Example Usage:
if __name__ == "__main__":
    solution = Solution()
    nums = [1, 7, 3, 6, 5, 6]
    result = solution.pivotIndex(nums)
    print(f"Pivot Index: {result}")

"""
⚡ Time Complexity: O(N)  
- We traverse the array once, so the complexity is linear.

💾 Space Complexity: O(1)  
- Constant space is used for left_sum and right_sum.
"""

