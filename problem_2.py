"""
LeetCode Problem: Greatest Common Divisor of Strings

Problem Statement:
For two strings s and t, we say "t divides s" if and only if s = t + t + ... + t (i.e., t is concatenated with itself one or more times).

Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.

Example 1:
Input: str1 = "ABCABC", str2 = "ABC"
Output: "ABC"

Example 2:
Input: str1 = "ABABAB", str2 = "ABAB"
Output: "AB"

Example 3:
Input: str1 = "LEET", str2 = "CODE"
Output: ""

Constraints:
1 <= str1.length, str2.length <= 1000
str1 and str2 consist of English uppercase letters.

Time Complexity: O(n + m) where n and m are the lengths of str1 and str2 respectively.
Space Complexity: O(1) since we only use a few extra variables.
"""

from math import gcd

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # If concatenation in different orders is not equal, return ""
        if str1 + str2 != str2 + str1:
            return ""
        
        # Find the greatest common divisor of lengths
        gcd_length = gcd(len(str1), len(str2))
        
        # Return the substring of length gcd_length
        return str1[:gcd_length]

# Example Usage
def main():
    solution = Solution()
    print(solution.gcdOfStrings("ABCABC", "ABC"))  # Output: "ABC"
    print(solution.gcdOfStrings("ABABAB", "ABAB"))  # Output: "AB"
    print(solution.gcdOfStrings("LEET", "CODE"))    # Output: ""

if __name__ == "__main__":
    main()
