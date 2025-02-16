"""
LeetCode Problem 345: Reverse Vowels of a String
Difficulty: Easy
LeetCode 75 - Problem 5

Problem Statement:
Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u' (both lowercase and uppercase).

Example 1:
Input: s = "IceCreAm"
Output: "AceCreIm"

Example 2:
Input: s = "leetcode"
Output: "leotcede"

Constraints:
1 <= s.length <= 3 * 10^5
s consists of printable ASCII characters.

Approach:
1. Convert the string into a list for mutability.
2. Use two pointers (`l` and `r`):
   - `l` starts from the left.
   - `r` starts from the right.
   - Swap vowels when both pointers find vowels.
3. Join the list back into a string and return the result.

Time Complexity: O(N) - We iterate through the string at most once.
Space Complexity: O(N) - Since strings are immutable in Python, we use a list.
"""

class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)  # Convert string to list for mutability
        l, r = 0, len(s) - 1
        vowels = set("aeiouAEIOU")  # Define a set of vowels
        
        while l < r:
            if s[l] not in vowels:
                l += 1
            elif s[r] not in vowels:
                r -= 1
            else:
                s[l], s[r] = s[r], s[l]  # Swap vowels
                l += 1
                r -= 1
        
        return "".join(s)  # Convert list back to string

# Example Usage
if __name__ == "__main__":
    solution = Solution()
    test_cases = ["IceCreAm", "leetcode", "hello", "aA"]
    for s in test_cases:
        print(f"Input: {s} -> Output: {solution.reverseVowels(s)}")
