"""
LeetCode Problem: Can Place Flowers (Problem #605)
Link: https://leetcode.com/problems/can-place-flowers/

Problem Statement:
You have a long flowerbed in which some of the plots are planted, and some are not. 
However, flowers cannot be planted in adjacent plots.

Given a flowerbed represented as a list containing 0s (empty) and 1s (occupied), and 
an integer `n`, return `True` if `n` new flowers can be planted without violating the 
no-adjacent-flowers rule, otherwise return `False`.

Example 1:
Input: flowerbed = [1, 0, 0, 0, 1], n = 1
Output: True

Example 2:
Input: flowerbed = [1, 0, 0, 0, 1], n = 2
Output: False

Constraints:
- 1 <= flowerbed.length <= 10^4
- flowerbed[i] is 0 or 1.
- 0 <= n <= flowerbed.length
"""

def canPlaceFlowers(flowerbed, n):
    """
    Function to check if n flowers can be planted in the given flowerbed.

    :param flowerbed: List[int] - The flowerbed representation (0 = empty, 1 = occupied).
    :param n: int - The number of flowers to plant.
    :return: bool - True if n flowers can be planted, otherwise False.

    Time Complexity: O(N) - We iterate through the flowerbed once.
    Space Complexity: O(1) - We modify the input array in-place without extra space.
    """
    
    # Add padding (0s) at the beginning and end to handle edge cases easily
    flowerbed = [0] + flowerbed + [0]
    count = 0  # To keep track of how many flowers we can plant
    
    # Iterate through the flowerbed (excluding the first and last added 0s)
    for i in range(1, len(flowerbed) - 1):
        # Check if the current position and its neighbors are empty (0)
        if flowerbed[i] == 0 and flowerbed[i-1] == 0 and flowerbed[i+1] == 0:
            flowerbed[i] = 1  # Plant a flower
            count += 1  # Increment the count
            
            # If we have planted enough flowers, return True early
            if count >= n:
                return True
    
    # If we exit the loop, check if we were able to plant at least 'n' flowers
    return count >= n

# Example Usage:
if __name__ == "__main__":
    print(canPlaceFlowers([1, 0, 0, 0, 1], 1))  # Output: True
    print(canPlaceFlowers([1, 0, 0, 0, 1], 2))  # Output: False
