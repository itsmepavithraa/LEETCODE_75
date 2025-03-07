# LeetCode Problem: Removing Stars From a String
# 
# **Problem Statement:**
# You are given a string `s`, which contains stars `*`.
# In one operation, you can:
# - Choose a star in `s`.
# - Remove the closest non-star character to its left, along with the star itself.
# Return the string after all stars have been removed.
#
# **Example:**
# ```
# Input: s = "leet**cod*e"
# Output: "lecoe"
# Explanation: Performing the removals:
# - The first star removes the 't'.
# - The second star removes the 'e'.
# - The third star removes the 'd'.
# ```
# 
# **Constraints:**
# - `1 <= s.length <= 10^5`
# - `s` consists of lowercase English letters and stars `*`.

from typing import List

class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        
        # Process each character
        for char in s:
            if char == '*':
                if stack:
                    stack.pop()  # Remove the last character if star is found
            else:
                stack.append(char)
                
        # Join the remaining characters
        return ''.join(stack)

# Time Complexity: O(n)
# - We traverse the string once, and each character is pushed or popped from the stack at most once.

# Space Complexity: O(n)
# - The stack stores the characters that are not removed, which can be up to the length of the string.

# Example usage:
if __name__ == "__main__":
    sol = Solution()
    s = "leet**cod*e"
    result = sol.removeStars(s)
    print("Resulting string after removing stars:", result)

# Output: Resulting string after removing stars: lecoe
