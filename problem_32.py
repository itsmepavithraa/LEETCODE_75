from typing import Optional

"""
Problem Statement: Maximum Twin Sum of a Linked List (LeetCode 2130)

In a linked list of even length n, a twin sum is defined as the sum of the i-th node and the (n - i - 1)-th node (0-based index).
Return the maximum twin sum of the linked list.

Example 1:
Input: head = [5, 4, 2, 1]
Output: 6
Explanation:
- Twin pairs are (5,1) and (4,2).
- Twin sums are 5 + 1 = 6 and 4 + 2 = 6.
- Maximum twin sum is 6.

Example 2:
Input: head = [4, 2, 2, 3]
Output: 7
Explanation:
- Twin pairs are (4,3) and (2,2).
- Twin sums are 4 + 3 = 7 and 2 + 2 = 4.
- Maximum twin sum is 7.

Time Complexity: O(N) - Finding the middle, reversing half, and computing max twin sum all take O(N).
Space Complexity: O(1) - Only a few pointers are used for in-place modifications.
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        # Step 1: Find the middle of the linked list
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        # Step 2: Reverse the second half of the linked list
        prev = None
        curr = slow
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp

        # Step 3: Find maximum twin sum
        head2 = prev  # Head of the reversed second half
        max_sum = 0
        while head2:
            max_sum = max(max_sum, head.val + head2.val)
            head = head.next
            head2 = head2.next

        return max_sum

# Helper function to create a linked list from a list
def create_linked_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

# Example usage with test cases
if __name__ == "__main__":
    test_cases = [
        [5, 4, 2, 1],  # Output: 6
        [4, 2, 2, 3],  # Output: 7
        [1, 100000],   # Output: 100001
        [10, 20, 30, 40, 50, 60]  # Output: 70
    ]

    solution = Solution()
    for test in test_cases:
        head = create_linked_list(test)
        result = solution.pairSum(head)
        print(f"Input: {test} => Maximum Twin Sum: {result}")
