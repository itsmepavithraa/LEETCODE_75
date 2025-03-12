# 🟢 Problem: Delete the Middle Node of a Linked List
# Given the head of a singly linked list, delete the middle node, 
# and return the head of the modified list.
# If there are two middle nodes, delete the second middle node.

# Example:
# Input: head = [1, 2, 3, 4, 5]
# Output: [1, 2, 4, 5]

# 🟠 Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteMiddle(self, head: ListNode) -> ListNode:
        # Edge case: If there's only one node, return None
        if head.next is None:
            return None
        
        # Initialize slow and fast pointers
        slow = fast = head
        prev = None
        
        # Traverse the list to find the middle node
        while fast and fast.next:
            prev = slow
            fast = fast.next.next
            slow = slow.next
        
        # Delete the middle node
        prev.next = prev.next.next
        
        # Return the modified list
        return head

# 🟡 Helper function to print the linked list
def printList(head):
    curr = head
    while curr:
        print(curr.val, end=" -> ")
        curr = curr.next
    print("None")

# 🟠 Test the function
if __name__ == "__main__":
    # Create a sample linked list: 1 -> 2 -> 3 -> 4 -> 5
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)

    print("Original Linked List:")
    printList(head)

    # Delete the middle node
    sol = Solution()
    updated_head = sol.deleteMiddle(head)

    print("\nLinked List after deleting the middle node:")
    printList(updated_head)
