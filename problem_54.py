# LeetCode 2300 - Successful Pairs of Spells and Potions
# You are given two positive integer arrays spells and potions, of length n and m respectively,
# where spells[i] represents the strength of the ith spell and potions[j] represents the strength of the jth potion.
# You are also given an integer success.
#
# A spell and potion pair is considered successful if the product of their strengths is at least success.
#
# Return an integer array pairs of length n where pairs[i] is the number of potions
# that will form a successful pair with the ith spell.

from typing import List

class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        pairs = []

        for spell in spells:
            low, high = 0, len(potions)
            while low < high:
                mid = (low + high) // 2
                if (potions[mid] * spell) >= success:
                    high = mid
                else:
                    low = mid + 1
            pairs.append(len(potions) - low)
        return pairs

# Test the function
if __name__ == "__main__":
    spells = [10, 20, 30]
    potions = [1, 2, 3, 4, 5]
    success = 100

    solution = Solution()
    result = solution.successfulPairs(spells, potions, success)
    print("Successful pairs for each spell:", result)

# ✅ Time Complexity:
#   - Sorting potions: O(m log m), where m is the length of potions
#   - For each spell, binary search: O(n log m), where n is the length of spells
#   - Total: O(m log m + n log m)

# ✅ Space Complexity:
#   - O(1) extra space (excluding output), O(n) including result array
