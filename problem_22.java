// Question: Determine if Two Strings Are Close

// Problem Statement:
// Two strings are considered "close" if you can transform one into the other using the following operations any number of times:
// 1. Swap any two existing characters.
// 2. Transform every occurrence of one character into another existing character (but you must apply this operation to all occurrences of that character).

// You are given two strings, word1 and word2. Return true if they are close, otherwise return false.

// Example 1:
// Input:
// word1 = "abc"
// word2 = "bca"
// Output: true

// Example 2:
// Input:
// word1 = "aabbcc"
// word2 = "ccbbaa"
// Output: true

// Example 3:
// Input:
// word1 = "cabbba"
// word2 = "aabbss"
// Output: false

import java.util.HashMap;
import java.util.Map;
import java.util.Arrays;
import java.util.Scanner;

public class problem_22 {

    public static boolean closeStrings(String word1, String word2) {
        if (word1.length() != word2.length()) {
            return false;
        }

        // Count character frequencies
        Map<Character, Integer> counts1 = new HashMap<>();
        Map<Character, Integer> counts2 = new HashMap<>();

        for (char c : word1.toCharArray()) {
            counts1.put(c, counts1.getOrDefault(c, 0) + 1);
        }
        for (char c : word2.toCharArray()) {
            counts2.put(c, counts2.getOrDefault(c, 0) + 1);
        }

        // Check if both strings have the same unique characters
        if (!counts1.keySet().equals(counts2.keySet())) {
            return false;
        }

        // Check if the frequency counts match (ignoring character identity)
        int[] freq1 = counts1.values().stream().mapToInt(Integer::intValue).toArray();
        int[] freq2 = counts2.values().stream().mapToInt(Integer::intValue).toArray();

        Arrays.sort(freq1);
        Arrays.sort(freq2);

        return Arrays.equals(freq1, freq2);
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Driver code to test the solution
        System.out.print("Enter the first string: ");
        String word1 = scanner.nextLine();
        System.out.print("Enter the second string: ");
        String word2 = scanner.nextLine();

        boolean result = closeStrings(word1, word2);
        System.out.println("Are the strings close? " + result);

        scanner.close();
    }
}

// Time Complexity: O(n log n)
// - Counting characters: O(n)
// - Comparing keys: O(1)
// - Sorting frequency values: O(n log n)

// Space Complexity: O(n)
// - Space for frequency counters

