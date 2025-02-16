"""
LeetCode Problem 151: Reverse Words in a String
Difficulty: Medium
LeetCode 75 - Problem 6

Problem Statement:
Given an input string s, reverse the order of the words.

A word is defined as a sequence of non-space characters. The words in `s` will be separated by at least one space.

You must return a string with:
1. Words in reverse order.
2. No leading or trailing spaces.
3. Only a single space between words.

Example 1:
Input: s = "the sky is blue"
Output: "blue is sky the"

Example 2:
Input: s = "  hello   world  "
Output: "world hello"

Example 3:
Input: s = "a good   example"
Output: "example good a"

Constraints:
- 1 <= s.length <= 10^4
- s consists of English letters and spaces.
- There is at least one word in s.

Approach:
1. Use `split()` to break the string into words while removing extra spaces.
2. Reverse the list of words.
3. Use `" ".join()` to reconstruct the reversed string.

Time Complexity: O(N) - We iterate through the string at most once.
Space Complexity: O(N) - Since strings are immutable in Python, we use a list.
"""

class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(s.split()[::-1])  # Split, reverse, and join words

# Example Usage
if __name__ == "__main__":
    solution = Solution()
    test_cases = ["the sky is blue", "  hello   world  ", "a good   example"]
    for s in test_cases:
        print(f"Input: {s} -> Output: {solution.reverseWords(s)}")
