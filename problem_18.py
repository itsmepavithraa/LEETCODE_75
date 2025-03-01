# LeetCode Problem: Find the Highest Altitude

# 🚩 Problem Statement:
# You are given an array `gain` of length `n` where `gain[i]` is the net gain in altitude between points `i` and `i + 1`.
# The altitude starts at 0. Return the highest altitude.

# 🧠 Example:
# Input: gain = [-5, 1, 5, 0, -7]
# Output: 1
# Explanation:
# Altitude changes: [0, -5, -4, 1, 1, -6]
# The highest altitude is 1.

# 🟩 Solution:

from typing import List

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        altitude = 0
        max_alt = 0
        for change in gain:
            altitude += change
            max_alt = max(max_alt, altitude)
        return max_alt

# 🔧 Test the solution:
if __name__ == "__main__":
    sol = Solution()
    gain = [-5, 1, 5, 0, -7]
    print("Highest Altitude:", sol.largestAltitude(gain))

# 🕒 Time Complexity: O(n)
# We traverse the `gain` array once, so the time complexity is linear.

# 🛢 Space Complexity: O(1)
# We use only a few variables, so the space complexity is constant.
