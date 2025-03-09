# LeetCode Problem: Decode String
# Given an encoded string, return its decoded string.
# The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is repeated exactly k times.
# You may assume the input string is always valid and contains only digits, letters, and square brackets.

# Example:
# Input: s = "3[a]2[bc]"
# Output: "aaabcbc"

# Time Complexity: O(N)
# Space Complexity: O(N)

class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        
        for char in s:
            if char != "]":
                stack.append(char)
            else:
                curr = ""
                
                while stack and stack[-1] != "[":
                    curr = stack.pop() + curr
                
                stack.pop()
                
                num = ""
                while stack and stack[-1].isdigit():
                    num = stack.pop() + num
                
                stack.append(curr * int(num))
        
        return "".join(stack)

# Test the solution
sol = Solution()
s = "3[a]2[bc]"
result = sol.decodeString(s)
print(result)  # Output: "aaabcbc"
