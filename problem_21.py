# 🟢 Question: Unique Number of Occurrences

# Given an array of integers arr, return true if the number of occurrences of each value in the array is unique, or false otherwise.

# 🛠️ Example:
# Input: arr = [1, 2, 2, 1, 1, 3]
# Output: True

# Explanation:
# - Frequency of 1: 3
# - Frequency of 2: 2
# - Frequency of 3: 1
# All frequencies are unique, so the result is True.

# 🔴 Example:
# Input: arr = [1, 2, 2, 3, 3]
# Output: False

# Explanation:
# - Frequency of 1: 1
# - Frequency of 2: 2
# - Frequency of 3: 2
# Frequency 2 repeats, so the result is False.

# 🚀 Solution:

from typing import List

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        freq_map = {}  # Create a dictionary to store frequencies
        
        # Count occurrences of each number
        for num in arr:
            if num in freq_map:
                freq_map[num] += 1
            else:
                freq_map[num] = 1
        
        # Store frequency values in a set
        freq_set = set(freq_map.values())
        
        # Check if set size matches the frequency map size
        return len(freq_set) == len(freq_map)

# ✅ Test Cases:
solution = Solution()
print(solution.uniqueOccurrences([1, 2, 2, 1, 1, 3]))  # Output: True
print(solution.uniqueOccurrences([1, 2, 2, 3, 3]))     # Output: False
print(solution.uniqueOccurrences([1, 2, 3]))           # Output: True
print(solution.uniqueOccurrences([3, 3, 3, 3]))        # Output: False

# 🟩 Time Complexity: O(N) — Iterating through the array and building the frequency map + checking set length.
# 🟩 Space Complexity: O(N) — Storing frequencies in a dictionary and a set.

# ✍️ This solution is efficient and works perfectly for the given problem!
