"""
# Problem: String Compression

## Description:
Given an array of characters `chars`, compress it using the following algorithm:

- Replace consecutive repeating characters with the character followed by its count.
- If a character appears once, keep it as is.
- The modification should be done **in-place**, using only constant extra space.

## Constraints:
- `1 <= len(chars) <= 10^4`
- `chars[i]` is a lowercase English letter.

## Example 1:
### Input:
    chars = ["a", "a", "b", "b", "c", "c", "c"]
### Output:
    6
### Explanation:
    The compressed list becomes ["a", "2", "b", "2", "c", "3"].

## Example 2:
### Input:
    chars = ["a"]
### Output:
    1
### Explanation:
    The compressed list remains ["a"].

## Example 3:
### Input:
    chars = ["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"]
### Output:
    4
### Explanation:
    The compressed list becomes ["a", "b", "1", "1"].

## Time Complexity:
- **O(N)**: We traverse the list once (`O(N)`) and modify it in-place (`O(1)` per character).

## Space Complexity:
- **O(1)**: The compression happens in-place, using only constant extra space.
"""

from typing import List

class Solution:
    def compress(self, chars: List[str]) -> int:
        write_index = 0  # Pointer to modify chars in-place
        read_index = 0   # Pointer to traverse chars

        while read_index < len(chars):
            current_char = chars[read_index]  # Current character
            count = 0  # Count occurrences of current_char

            # Count consecutive occurrences of current_char
            while read_index < len(chars) and chars[read_index] == current_char:
                count += 1
                read_index += 1  # Move to the next character

            # Write the character
            chars[write_index] = current_char
            write_index += 1

            # Write the count only if it's greater than 1
            if count > 1:
                for digit in str(count):  # Convert count to string and store each digit
                    chars[write_index] = digit
                    write_index += 1

        return write_index  # Return new length of chars

# Example usage
if __name__ == "__main__":
    chars = ["a", "a", "b", "b", "c", "c", "c"]
    solution = Solution()
    new_length = solution.compress(chars)
    print("Compressed List:", chars[:new_length])
    print("New Length:", new_length)
