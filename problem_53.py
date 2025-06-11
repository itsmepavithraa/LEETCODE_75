"""
Problem: 374. Guess Number Higher or Lower

We are playing the Guess Game. The game is as follows:

I pick a number from 1 to n. You have to guess which number I picked.

Every time you guess wrong, I will tell you whether the number I picked is higher or lower than your guess.

You call a pre-defined API int guess(int num), which returns:
-1 : My number is lower than your guess
 1 : My number is higher than your guess
 0 : Your guess is correct

You need to implement:
    def guessNumber(n: int) -> int

Example:
Input: n = 10, pick = 6
Output: 6

Time Complexity: O(log n) - Because we halve the search range every iteration (Binary Search).
Space Complexity: O(1) - Only a few integer variables used regardless of input size.
"""

# --- Mock API for testing ---
# Replace this value to simulate the picked number
PICKED_NUMBER = 6

def guess(num: int) -> int:
    if num > PICKED_NUMBER:
        return -1
    elif num < PICKED_NUMBER:
        return 1
    else:
        return 0

# --- Binary Search Solution ---
class Solution:
    def guessNumber(self, n: int) -> int:
        low, high = 1, n
        while low <= high:
            mid = (low + high) // 2
            result = guess(mid)
            if result == 0:
                return mid
            elif result == 1:
                low = mid + 1
            else:
                high = mid - 1
        return -1  # Shouldn't happen if input is valid

# --- Test the solution ---
if __name__ == "__main__":
    n = 10
    solution = Solution()
    print("Guessed Number:", solution.guessNumber(n))
