"""
Question:
Implement a class called `SmallestInfiniteSet` that simulates an infinite set of positive integers starting from 1.

The class should support the following operations:

1. `popSmallest()`: Removes and returns the smallest number in the set.
2. `addBack(num)`: Adds a previously removed number back into the set. If the number is already present, do nothing.

Example:
obj = SmallestInfiniteSet()
print(obj.popSmallest())  # Output: 1
print(obj.popSmallest())  # Output: 2
obj.addBack(1)            # Add 1 back to the set
print(obj.popSmallest())  # Output: 1
print(obj.popSmallest())  # Output: 3
print(obj.popSmallest())  # Output: 4

Constraints:
- `1 <= num <= 1000`
- At most 1000 calls will be made to `popSmallest` and `addBack`.
"""

class SmallestInfiniteSet:
    def __init__(self):
        self.smallest = 1               # Next smallest number to return
        self.removed = set()           # Set to track removed (popped) numbers

    def popSmallest(self) -> int:
        ret = self.smallest            # Store current smallest to return
        self.removed.add(ret)          # Mark it as removed
        self.smallest += 1             # Move to next number

        while self.smallest in self.removed:
            self.smallest += 1         # Skip numbers already removed

        return ret                     # Return the popped smallest number

    def addBack(self, num: int) -> None:
        if num in self.removed:        # Only add back if it was removed
            self.removed.remove(num)   # Remove from the removed set

            if num < self.smallest:
                self.smallest = num    # Update smallest if needed

# Example usage
obj = SmallestInfiniteSet()
print(obj.popSmallest())  # Output: 1
print(obj.popSmallest())  # Output: 2
obj.addBack(1)            # Add 1 back to the set
print(obj.popSmallest())  # Output: 1
print(obj.popSmallest())  # Output: 3
print(obj.popSmallest())  # Output: 4

"""
Time Complexity:
- popSmallest(): O(1) on average, worst-case O(n) if many numbers are added back and skipped
- addBack(num): O(1)

Space Complexity:
- O(n), where n is the number of elements removed or added back (up to 1000 as per constraints)
"""
