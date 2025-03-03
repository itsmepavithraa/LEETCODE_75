from typing import List

# Question: Find the Difference of Two Arrays
# 
# You are given two integer arrays `nums1` and `nums2`. 
# The task is to return a list of two lists:
# - The first list contains elements that are in `nums1` but not in `nums2`.
# - The second list contains elements that are in `nums2` but not in `nums1`.
# 
# Each element in the result must be unique, and you may return the result in any order.
# 
# Example:
# Input: nums1 = [1, 2, 3], nums2 = [2, 4, 6]
# Output: [[1, 3], [4, 6]]


# Approach 1: Using Loop and Manual Check
class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        nums1 = set(nums1)
        nums2 = set(nums2)
        ans1 = []
        for num in nums1:
            if num not in nums2:
                ans1.append(num)
            else:
                nums2.remove(num)
        return [ans1, list(nums2)]


# Approach 2: Using Set Operations
def findDifference(nums1, nums2):
    set1, set2 = set(nums1), set(nums2)
    diff1 = list(set1 - set2)
    diff2 = list(set2 - set1)
    return [diff1, diff2]


# Example usage
nums1 = [1, 2, 3]
nums2 = [2, 4, 6]

# Test both approaches
sol = Solution()
result1 = sol.findDifference(nums1, nums2)
print("Approach 1 (Manual Check) Result:", result1)

result2 = findDifference(nums1, nums2)
print("Approach 2 (Set Operations) Result:", result2)

# Time Complexity: O(m + n)
# Space Complexity: O(m + n)

# Let me know if you’d like me to refine the code or explain further! ✨
