// LeetCode Problem: Decode String
// Given an encoded string, return its decoded string.
// The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is repeated exactly k times.
// You may assume the input string is always valid and contains only digits, letters, and square brackets.

// Example:
// Input: s = "3[a]2[bc]"
// Output: "aaabcbc"

// Time Complexity: O(N)
// Space Complexity: O(N)

import java.util.Stack;

public class problem_26 {
    public String decodeString(String s) {
        Stack<String> stack = new Stack<>();
        
        for (char ch : s.toCharArray()) {
            if (ch != ']') {
                stack.push(String.valueOf(ch));
            } else {
                StringBuilder curr = new StringBuilder();
                
                while (!stack.isEmpty() && !stack.peek().equals("[")) {
                    curr.insert(0, stack.pop());
                }
                
                stack.pop(); 
                
                StringBuilder num = new StringBuilder();
                while (!stack.isEmpty() && Character.isDigit(stack.peek().charAt(0))) {
                    num.insert(0, stack.pop());
                }
                
                int count = Integer.parseInt(num.toString());
                String repeated = curr.toString().repeat(count);
                
                stack.push(repeated);
            }
        }
        
        StringBuilder result = new StringBuilder();
        while (!stack.isEmpty()) {
            result.insert(0, stack.pop());
        }
        
        return result.toString();
    }

    public static void main(String[] args) {
        problem_26 sol = new problem_26();
        String s = "3[a]2[bc]";
        String result = sol.decodeString(s);
        System.out.println(result);  // Output: "aaabcbc"
    }
}

