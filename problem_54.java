// LeetCode 2300 - Successful Pairs of Spells and Potions
// You are given two positive integer arrays spells and potions, of length n and m respectively,
// where spells[i] represents the strength of the ith spell and potions[j] represents the strength of the jth potion.
// You are also given an integer success.
//
// A spell and potion pair is considered successful if the product of their strengths is at least success.
//
// Return an integer array pairs of length n where pairs[i] is the number of potions
// that will form a successful pair with the ith spell.

import java.util.Arrays;

public class problem_54 {
    public int[] successfulPairs(int[] spells, int[] potions, int success) {
        Arrays.sort(potions);
        int[] pairs = new int[spells.length];

        for (int i = 0; i < spells.length; i++) {
            int spell = spells[i];
            int low = 0, high = potions.length;

            while (low < high) {
                int mid = (low + high) / 2;
                if ((long) potions[mid] * spell >= success) {
                    high = mid;
                } else {
                    low = mid + 1;
                }
            }
            pairs[i] = potions.length - low;
        }

        return pairs;
    }

    // Main method to test the solution
    public static void main(String[] args) {
        int[] spells = {10, 20, 30};
        int[] potions = {1, 2, 3, 4, 5};
        int success = 100;

        problem_54 solution = new problem_54();
        int[] result = solution.successfulPairs(spells, potions, success);

        System.out.print("Successful pairs for each spell: ");
        for (int val : result) {
            System.out.print(val + " ");
        }
    }
}

/*
✅ Time Complexity:
   - Sorting potions: O(m log m), where m = potions.length
   - For each spell, binary search: O(n log m), where n = spells.length
   - Total: O(m log m + n log m)

✅ Space Complexity:
   - O(1) extra space (excluding output), O(n) for result array
*/
