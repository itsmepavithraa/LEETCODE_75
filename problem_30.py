# 🧠 Odd Even Linked List Problem

# 🔸 Question:
# Given the head of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices,
# and return the reordered list. The first node is considered odd, the second node even, and so on.
# 
# Example:
# Input: head = [1, 2, 3, 4, 5]
# Output: [1, 3, 5, 2, 4]

from typing import Optional

# 🟩 Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        odd = head
        even = even_head = head.next
        while even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
        odd.next = even_head
        return head

# 🟢 Test the solution
if __name__ == "__main__":
    # Create the linked list: 1 -> 2 -> 3 -> 4 -> 5
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))

    # Call the function
    solution = Solution()
    result = solution.oddEvenList(head)

    # Print the result
    print("Odd Even Linked List:")
    while result:
        print(result.val, end=" -> " if result.next else "")
        result = result.next
