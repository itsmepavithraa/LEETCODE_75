// LeetCode 75: Maximum Number of Vowels in a Substring of Given Length

// Problem Statement:
// Given a string s and an integer k, return the maximum number of vowel letters in any substring of length k.
// Vowels: 'a', 'e', 'i', 'o', 'u'

// Example:
// Input: s = "abciiidef", k = 3
// Output: 3
// Explanation: The substring "iii" contains 3 vowels.

// Java Solution:

public class problem_15 {
    public static int maxVowels(String s, int k) {
        // Define a set of vowels
        String vowels = "aeiou";
        
        // Initialize counters
        int maxVowels = 0;
        int currentVowels = 0;

        // Count vowels in the initial window of size k
        for (int i = 0; i < k; i++) {
            if (vowels.indexOf(s.charAt(i)) != -1) {
                currentVowels++;
            }
        }
        
        // Set the initial count as the max count
        maxVowels = currentVowels;

        // Slide the window across the string
        for (int i = k; i < s.length(); i++) {
            // Add the new character to the window
            if (vowels.indexOf(s.charAt(i)) != -1) {
                currentVowels++;
            }

            // Remove the character going out of the window
            if (vowels.indexOf(s.charAt(i - k)) != -1) {
                currentVowels--;
            }

            // Update the maximum vowels count
            maxVowels = Math.max(maxVowels, currentVowels);
        }

        return maxVowels;
    }

    public static void main(String[] args) {
        String s = "abciiidef";
        int k = 3;
        System.out.println(maxVowels(s, k)); // Output: 3
    }
}

// Time Complexity: O(N) — We traverse the string once with the sliding window.
// Space Complexity: O(1) — Constant space is used for counters.

