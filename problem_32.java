/*
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
*/

class ListNode {
    int val;
    ListNode next;
    ListNode(int val) {
        this.val = val;
        this.next = null;
    }
}

class Solution {
    public int pairSum(ListNode head) {
        // Step 1: Find the middle of the linked list
        ListNode slow = head, fast = head;
        while (fast != null && fast.next != null) {
            fast = fast.next.next;
            slow = slow.next;
        }

        // Step 2: Reverse the second half of the linked list
        ListNode prev = null, curr = slow;
        while (curr != null) {
            ListNode tmp = curr.next;
            curr.next = prev;
            prev = curr;
            curr = tmp;
        }

        // Step 3: Find maximum twin sum
        ListNode head2 = prev; // Head of the reversed second half
        int maxSum = 0;
        while (head2 != null) {
            maxSum = Math.max(maxSum, head.val + head2.val);
            head = head.next;
            head2 = head2.next;
        }

        return maxSum;
    }
}

// Helper class to create and test the linked list
public class problem_32 {
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

    public static void main(String[] args) {
        int[][] testCases = {
            {5, 4, 2, 1},  // Output: 6
            {4, 2, 2, 3},  // Output: 7
            {1, 100000},   // Output: 100001
            {10, 20, 30, 40, 50, 60}  // Output: 70
        };

        Solution solution = new Solution();
        for (int[] test : testCases) {
            ListNode head = createLinkedList(test);
            int result = solution.pairSum(head);
            System.out.println("Input: " + java.util.Arrays.toString(test) + " => Maximum Twin Sum: " + result);
        }
    }
}
