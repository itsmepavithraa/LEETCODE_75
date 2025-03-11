from collections import deque

# LeetCode Problem: Dota2 Senate

# 🧠 Question:
# In the world of Dota2, there are two parties: Radiant and Dire.
# The Senate consists of senators from these two parties, and each senator can vote to ban one senator from the opposite party.
# Votes are cast in the order the senators appear in the input string.

# The game proceeds in rounds:
# - Each senator can either ban one senator from the opposite party or be banned.
# - The senator with the smaller index gets to vote first.
# - The winning senator stays in the game and re-enters the queue with their index + length of the string (`n`).

# You are given a string `senate` representing senators:
# - 'R' for Radiant
# - 'D' for Dire

# Return the winning party after all the bans are complete!

# 🔑 Example:
# Input: "RDD"
# Output: "Dire"

# Explanation:
# - R bans D (at index 1).
# - D (index 2) bans R.
# - Only D is left, so Dire wins.

# 🚀 Solution:
class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        dire = deque()
        radiant = deque()
        n = len(senate)
        
        # Fill queues with senator indices
        for i in range(n):
            if senate[i] == "D":
                dire.append(i)
            else:
                radiant.append(i)
        
        # Process the bans
        while dire and radiant:
            d = dire.popleft()
            r = radiant.popleft()
            
            # The senator with the smaller index stays
            if r < d:
                radiant.append(r + n)
            else:
                dire.append(d + n)
        
        # Return the winning party
        return "Radiant" if radiant else "Dire"

# 🧩 Test the function
senate = "RDD"
solution = Solution()
print(solution.predictPartyVictory(senate))  # Output: "Dire"

# 📊 Time Complexity: O(n)
# - Each senator is processed once, and queue operations are O(1).
# - So the algorithm runs in linear time.

# 🛢️ Space Complexity: O(n)
# - We use two queues to store the indices of senators.

