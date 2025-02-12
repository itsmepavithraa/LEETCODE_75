"""
LeetCode Problem: Merge Strings Alternately

Problem Statement:
You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, 
starting with word1. If a string is longer than the other, append the additional letters onto the end of 
the merged string. Return the merged string.

Example 1:
Input: word1 = "abc", word2 = "pqr"
Output: "apbqcr"

Example 2:
Input: word1 = "ab", word2 = "pqrs"
Output: "apbqrs"

Example 3:
Input: word1 = "abcd", word2 = "pq"
Output: "apbqcd"

Time Complexity: O(n + m) where n and m are the lengths of word1 and word2 respectively.
Space Complexity: O(n + m) for storing the result.
"""

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i, j = 0, 0
        res = []
        
        while i < len(word1) and j < len(word2):
            res.append(word1[i])
            res.append(word2[j])
            i += 1
            j += 1
        
        res.append(word1[i:])  # Append remaining characters from word1
        res.append(word2[j:])  # Append remaining characters from word2
        
        return "".join(res)

# Example Usage
def main():
    solution = Solution()
    word1 = "abc"
    word2 = "pqr"
    print(solution.mergeAlternately(word1, word2))  # Output: "apbqcr"

if __name__ == "__main__":
    main()
