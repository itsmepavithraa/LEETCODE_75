"""
Problem: Reverse Linked List (LeetCode 206)

Given the head of a singly linked list, reverse the list and return its head.

Example 1:
Input: head = [1, 2, 3, 4, 5]
Output: [5, 4, 3, 2, 1]

Example 2:
Input: head = [1, 2]
Output: [2, 1]

Example 3:
Input: head = []
Output: []

Time Complexity: O(N) - We traverse the linked list once.
Space Complexity: O(1) - In-place reversal, using only a few pointers.
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        curr = head
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev

# Function to create a linked list from a list
def create_linked_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

# Function to print the linked list
def print_linked_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    print(result)

# Test case
head = create_linked_list([1, 2, 3, 4, 5])
solution = Solution()
reversed_head = solution.reverseList(head)
print_linked_list(reversed_head)  # Output: [5, 4, 3, 2, 1]
