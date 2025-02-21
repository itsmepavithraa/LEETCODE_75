"""
LeetCode Problem: Is Subsequence

Problem Statement:
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string 
by deleting some (can be none) of the characters without disturbing the relative positions 
of the remaining characters.

Example 1:
Input: s = "abc", t = "ahbgdc"
Output: True

Example 2:
Input: s = "axc", t = "ahbgdc"
Output: False

Constraints:
- 0 <= len(s) <= 100
- 0 <= len(t) <= 10^4
- s and t consist only of lowercase English letters.
"""

def isSubsequence(s: str, t: str) -> bool:
    """
    Determines if s is a subsequence of t using a two-pointer approach.
    
    :param s: The subsequence string
    :param t: The main string
    :return: True if s is a subsequence of t, False otherwise
    """
    i, j = 0, 0  # Pointers for s and t

    while i < len(s) and j < len(t):
        if s[i] == t[j]:  # If characters match, move both pointers
            i += 1
        j += 1  # Always move pointer in t

    return i == len(s)  # If we matched all characters in s, return True

# Example usage:
if __name__ == "__main__":
    s = "abc"
    t = "ahbgdc"
    print(isSubsequence(s, t))  # Output: True

    s = "axc"
    t = "ahbgdc"
    print(isSubsequence(s, t))  # Output: False

"""
Time Complexity: O(n) - We traverse t at most once (where n = len(t)).
Space Complexity: O(1) - We use only two pointers, no extra space.
"""
