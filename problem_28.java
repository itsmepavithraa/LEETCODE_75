import java.util.LinkedList;
import java.util.Queue;

public class problem_28 {

    // 🧠 Problem Statement:
    // In the Dota2 Senate, there are two parties: Radiant and Dire.
    // Senators vote to ban one senator from the opposite party.
    // The senator who appears earlier gets the chance to ban first.
    // The winner is the party that completely bans all the members of the opposite party.

    // 🟩 Example:
    // Input: "RDD"
    // Output: "Dire"

    // 🚀 Solution:
    public String predictPartyVictory(String senate) {
        Queue<Integer> radiant = new LinkedList<>();
        Queue<Integer> dire = new LinkedList<>();

        int n = senate.length();

        // Fill the queues with indices of 'R' and 'D'
        for (int i = 0; i < n; i++) {
            if (senate.charAt(i) == 'R') {
                radiant.add(i);
            } else {
                dire.add(i);
            }
        }

        // Process the bans
        while (!radiant.isEmpty() && !dire.isEmpty()) {
            int rIndex = radiant.poll();
            int dIndex = dire.poll();

            // The senator with the smaller index gets to ban the other
            if (rIndex < dIndex) {
                radiant.add(rIndex + n);
            } else {
                dire.add(dIndex + n);
            }
        }

        // Return the winning party
        return radiant.isEmpty() ? "Dire" : "Radiant";
    }

    // 🧩 Test the function
    public static void main(String[] args) {
        problem_28 solution = new problem_28();
        
        String senate = "RDD";
        System.out.println(solution.predictPartyVictory(senate));  // Output: "Dire"
    }

    // 📊 Time Complexity: O(n)
    // - Each senator is processed once, and queue operations are O(1).

    // 🛢️ Space Complexity: O(n)
    // - We use two queues to store the indices of senators.
}
