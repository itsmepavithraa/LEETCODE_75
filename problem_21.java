// 🟢 Question: Unique Number of Occurrences

// Given an array of integers arr, return true if the number of occurrences of each value in the array is unique, or false otherwise.

// 🛠️ Example:
// Input: arr = [1, 2, 2, 1, 1, 3]
// Output: true

// Explanation:
// - Frequency of 1: 3
// - Frequency of 2: 2
// - Frequency of 3: 1
// All frequencies are unique, so the result is true.

// 🔴 Example:
// Input: arr = [1, 2, 2, 3, 3]
// Output: false

// Explanation:
// - Frequency of 1: 1
// - Frequency of 2: 2
// - Frequency of 3: 2
// Frequency 2 repeats, so the result is false.

import java.util.HashMap;
import java.util.HashSet;

public class problem_21 {
    public boolean uniqueOccurrences(int[] arr) {
        // Create a frequency map
        HashMap<Integer, Integer> freqMap = new HashMap<>();

        // Count occurrences of each number
        for (int num : arr) {
            freqMap.put(num, freqMap.getOrDefault(num, 0) + 1);
        }

        // Store frequency values in a set
        HashSet<Integer> freqSet = new HashSet<>(freqMap.values());

        // Check if set size matches the frequency map size
        return freqSet.size() == freqMap.size();
    }

    public static void main(String[] args) {
        problem_21 solution = new problem_21();
        
        // ✅ Test Cases
        System.out.println(solution.uniqueOccurrences(new int[]{1, 2, 2, 1, 1, 3})); // Output: true
        System.out.println(solution.uniqueOccurrences(new int[]{1, 2, 2, 3, 3}));   // Output: false
        System.out.println(solution.uniqueOccurrences(new int[]{1, 2, 3}));         // Output: true
        System.out.println(solution.uniqueOccurrences(new int[]{3, 3, 3, 3}));      // Output: false
    }
}

// 🟩 Time Complexity: O(N) — Iterating through the array and building the frequency map + checking set length.
// 🟩 Space Complexity: O(N) — Storing frequencies in a HashMap and a HashSet.

// ✍️ This solution is efficient and works perfectly for the given problem!

