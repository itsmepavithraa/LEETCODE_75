# Question: Determine if Two Strings Are Close

# Problem Statement:
# Two strings are considered "close" if you can transform one into the other using the following operations any number of times:
# 1. Swap any two existing characters.
# 2. Transform every occurrence of one character into another existing character (but you must apply this operation to all occurrences of that character).

# You are given two strings, word1 and word2. Return True if they are close, otherwise return False.

# Example 1:
# Input:
# word1 = "abc"
# word2 = "bca"
# Output: True

# Example 2:
# Input:
# word1 = "aabbcc"
# word2 = "ccbbaa"
# Output: True

# Example 3:
# Input:
# word1 = "cabbba"
# word2 = "aabbss"
# Output: False

# Python Solution:
from collections import Counter

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        
        counts1 = Counter(word1)
        counts2 = Counter(word2)
        
        return (counts1.keys() == counts2.keys()) and (sorted(counts1.values()) == sorted(counts2.values()))

# Driver code to test the solution
if __name__ == "__main__":
    solution = Solution()
    word1 = input("Enter the first string: ")
    word2 = input("Enter the second string: ")
    
    result = solution.closeStrings(word1, word2)
    print(f"Are the strings close? {result}")

# Time Complexity: O(n log n)
# - Counting characters: O(n)
# - Comparing keys: O(1)
# - Sorting frequency values: O(n log n)

# Space Complexity: O(n)
# - Space for frequency counters

