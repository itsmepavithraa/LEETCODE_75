# LeetCode 75: Maximum Number of Vowels in a Substring of Given Length

# Problem Statement:
# Given a string s and an integer k, return the maximum number of vowel letters in any substring of length k.
# Vowels: 'a', 'e', 'i', 'o', 'u'

# Example:
# Input: s = "abciiidef", k = 3
# Output: 3
# Explanation: The substring "iii" contains 3 vowels.

# Python Solution:

def maxVowels(s: str, k: int) -> int:
    # Define a set of vowels for quick lookup
    vowels = set("aeiou")
    
    # Initialize variables to keep track of counts
    max_vowels = 0  # Stores the maximum number of vowels found
    current_vowels = 0  # Counts vowels in the current window

    # Count vowels in the initial window of size k
    for i in range(k):
        if s[i] in vowels:
            current_vowels += 1
    
    # Set the initial count as the max count
    max_vowels = current_vowels

    # Slide the window across the string
    for i in range(k, len(s)):
        # Add the new character to the window
        if s[i] in vowels:
            current_vowels += 1
        
        # Remove the character going out of the window
        if s[i - k] in vowels:
            current_vowels -= 1
        
        # Update the maximum vowels count
        max_vowels = max(max_vowels, current_vowels)

    return max_vowels

# Example usage
s = "abciiidef"
k = 3
print(maxVowels(s, k))  # Output: 3

# Time Complexity: O(N) — We traverse the string once with the sliding window.
# Space Complexity: O(1) — Constant space is used for the vowel set and counters.
