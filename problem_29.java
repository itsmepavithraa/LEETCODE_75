// 🟢 Problem: Delete the Middle Node of a Linked List
// Given the head of a singly linked list, delete the middle node, 
// and return the head of the modified list.
// If there are two middle nodes, delete the second middle node.

// Example:
// Input: head = [1, 2, 3, 4, 5]
// Output: [1, 2, 4, 5]

class ListNode {
    int val;
    ListNode next;
    
    ListNode(int val) {
        this.val = val;
        this.next = null;
    }
}

public class problem_29 {

    // 🟠 Function to delete the middle node
    public ListNode deleteMiddle(ListNode head) {
        // Edge case: If there's only one node, return null
        if (head == null || head.next == null) {
            return null;
        }

        // Initialize slow and fast pointers
        ListNode slow = head;
        ListNode fast = head;
        ListNode prev = null;

        // Traverse the list to find the middle node
        while (fast != null && fast.next != null) {
            prev = slow;
            slow = slow.next;
            fast = fast.next.next;
        }

        // Delete the middle node
        prev.next = slow.next;

        return head;
    }

    // 🟡 Helper function to print the linked list
    public void printList(ListNode head) {
        ListNode current = head;
        while (current != null) {
            System.out.print(current.val + " -> ");
            current = current.next;
        }
        System.out.println("None");
    }

    public static void main(String[] args) {
        problem_29 solution = new problem_29();

        // Create a sample linked list: 1 -> 2 -> 3 -> 4 -> 5
        ListNode head = new ListNode(1);
        head.next = new ListNode(2);
        head.next.next = new ListNode(3);
        head.next.next.next = new ListNode(4);
        head.next.next.next.next = new ListNode(5);

        System.out.println("Original Linked List:");
        solution.printList(head);

        // Delete the middle node
        head = solution.deleteMiddle(head);

        System.out.println("\nLinked List after deleting the middle node:");
        solution.printList(head);
    }
}
