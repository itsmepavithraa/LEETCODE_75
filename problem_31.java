/*
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
*/

// Definition for singly-linked list.
class ListNode {
    int val;
    ListNode next;
    ListNode(int val) {
        this.val = val;
        this.next = null;
    }
}

class Solution {
    public ListNode reverseList(ListNode head) {
        ListNode prev = null;
        ListNode curr = head;
        while (curr != null) {
            ListNode temp = curr.next;
            curr.next = prev;
            prev = curr;
            curr = temp;
        }
        return prev;
    }
}

// Utility class for testing
public class problem_31 {
    // Function to create a linked list from an array
    public static ListNode createLinkedList(int[] arr) {
        if (arr.length == 0) return null;
        ListNode head = new ListNode(arr[0]);
        ListNode current = head;
        for (int i = 1; i < arr.length; i++) {
            current.next = new ListNode(arr[i]);
            current = current.next;
        }
        return head;
    }

    // Function to print a linked list
    public static void printLinkedList(ListNode head) {
        while (head != null) {
            System.out.print(head.val + " ");
            head = head.next;
        }
        System.out.println();
    }

    public static void main(String[] args) {
        int[] arr = {1, 2, 3, 4, 5};
        ListNode head = createLinkedList(arr);
        Solution solution = new Solution();
        ListNode reversedHead = solution.reverseList(head);
        printLinkedList(reversedHead);  // Output: 5 4 3 2 1
    }
}
