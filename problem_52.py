# LeetCode 2462: Total Cost to Hire K Workers

# Problem:
# You are given a 0-indexed integer array costs where costs[i] is the cost of hiring the i-th worker.
# You are also given two integers k and candidates.
# You want to hire exactly k workers from either the beginning or the end of the costs list.
# To do this, you will run the following steps exactly k times:
#
# - In each step, choose candidates workers from the beginning of the list who have not been hired.
# - Choose candidates workers from the end of the list who have not been hired.
# - Among the selected workers, pick the one with the lowest cost.
#   - If there is a tie, choose the worker with the smaller index.
# - Remove the chosen worker from the list (so they cannot be chosen again).
#
# Return the total cost to hire exactly k workers.

# Time Complexity:
# O(k * log(candidates))
# - At most 2 * candidates elements in the heaps.
# - For each of the k iterations, we do heap push and pop operations (log candidates time).

# Space Complexity:
# O(candidates)
# - Two heaps (left and right), each with up to 'candidates' elements.

import heapq
from typing import List

class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        i, j = 0, len(costs) - 1           # Two pointers: i from left, j from right
        left, right = [], []              # Min-heaps for left and right candidates
        total = 0                         # Total cost initialized

        while k:                          # Loop until k workers are hired
            # Fill left heap from the front
            while len(left) < candidates and i <= j:
                heapq.heappush(left, costs[i])  # Push to left heap
                i += 1                          # Move left pointer

            # Fill right heap from the end
            while len(right) < candidates and j >= i:
                heapq.heappush(right, costs[j]) # Push to right heap
                j -= 1                          # Move right pointer

            # Choose the cheaper of the two heaps
            if not right or (left and left[0] <= right[0]):
                total += heapq.heappop(left)    # Hire from left
            else:
                total += heapq.heappop(right)   # Hire from right

            k -= 1                              # One worker hired

        return total                            # Return total hiring cost

# Example 1:
# Input: costs = [17,12,10,2,7,2,11,20,8], k = 3, candidates = 4
# Step-by-step hires: 2 (right), 2 (left), 7 (left)
# Output: 11
costs = [17, 12, 10, 2, 7, 2, 11, 20, 8]
k = 3
candidates = 4
sol = Solution()
print(sol.totalCost(costs, k, candidates))  # Output: 11
