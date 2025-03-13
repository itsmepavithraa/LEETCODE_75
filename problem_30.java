// 🧠 Odd Even Linked List Problem

// 🔸 Question:
// Given the head of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices,
// and return the reordered list. The first node is considered odd, the second node even, and so on.
// 
// Example:
// Input: head = [1, 2, 3, 4, 5]
// Output: [1, 3, 5, 2, 4]

public class problem_30 {

    // 🟩 Definition for singly-linked list.
    static class ListNode {
        int val;
        ListNode next;

        ListNode(int val) {
            this.val = val;
            this.next = null;
        }
    }

    public static ListNode oddEvenList(ListNode head) {
        if (head == null || head.next == null) {
            return head;
        }

        ListNode odd = head;
        ListNode even = head.next;
        ListNode evenHead = even;

        while (even != null && even.next != null) {
            odd.next = even.next;
            odd = odd.next;
            even.next = odd.next;
            even = even.next;
        }

        odd.next = evenHead;
        return head;
    }

    public static void main(String[] args) {
        // 🟢 Test the solution
        ListNode head = new ListNode(1);
        head.next = new ListNode(2);
        head.next.next = new ListNode(3);
        head.next.next.next = new ListNode(4);
        head.next.next.next.next = new ListNode(5);

        ListNode result = oddEvenList(head);

        // Print the result
        System.out.println("Odd Even Linked List:");
        while (result != null) {
            System.out.print(result.val + (result.next != null ? " -> " : ""));
            result = result.next;
        }
    }
}

// ⏱️ Time Complexity: O(N) — We traverse the entire list once.
// 🛢️ Space Complexity: O(1) — No extra space, we just rearrange the pointers.
