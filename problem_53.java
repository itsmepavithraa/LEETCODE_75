/**
 * Problem: 374. Guess Number Higher or Lower
 *
 * We are playing the Guess Game. The game is as follows:
 * I pick a number from 1 to n. You have to guess which number I picked.
 * 
 * Every time you guess wrong, I will tell you whether the number I picked
 * is higher or lower than your guess.
 *
 * You are given a predefined API:
 *     int guess(int num):
 *         - returns -1 if num is higher than the picked number
 *         - returns 1 if num is lower than the picked number
 *         - returns 0 if num is equal to the picked number
 *
 * You must implement:
 *     public int guessNumber(int n)
 *
 * Time Complexity: O(log n) - because we reduce the search space by half each iteration (Binary Search).
 * Space Complexity: O(1) - only a few variables are used.
 */

public class problem_53 {

    // --- Mock API for testing ---
    static int PICKED_NUMBER = 6;

    public static int guess(int num) {
        if (num > PICKED_NUMBER) return -1;
        else if (num < PICKED_NUMBER) return 1;
        else return 0;
    }

    // --- Binary Search Solution ---
    public int guessNumber(int n) {
        int low = 1, high = n;

        while (low <= high) {
            int mid = low + (high - low) / 2;
            int result = guess(mid);

            if (result == 0) return mid;
            else if (result == 1) low = mid + 1;
            else high = mid - 1;
        }

        return -1; // Should not happen if the picked number is within the range
    }

    // --- Test the solution ---
    public static void main(String[] args) {
        int n = 10;
        problem_53 solution = new problem_53();
        System.out.println("Guessed Number: " + solution.guessNumber(n));
    }
}
