"""
🔹 Problem: Keys and Rooms (LeetCode 841 - Medium)

You are given an array `rooms` where `rooms[i]` is a list of keys in room `i`. 
Each key unlocks another room. All rooms are locked initially, except for room `0`.  

Your task is to return `True` if you can visit all rooms, otherwise return `False`.  

### Example 1:
Input: rooms = [[1],[2],[3],[]]
Output: True
Explanation:  
- Start in room `0`, collect key `1`.  
- Go to room `1`, collect key `2`.  
- Go to room `2`, collect key `3`.  
- Go to room `3`, all rooms are visited.

### Example 2:
Input: rooms = [[1,3],[3,0,1],[2],[0]]
Output: False
Explanation:  
- Start in room `0`, collect keys `1` and `3`.  
- Room `2` is never reached.

--------------------------------------------------------------
🔹 Time Complexity: O(N + E)
    - N = Number of rooms
    - E = Number of keys in total (edges in the graph)
    - Each room is visited once, and all keys (edges) are processed once.

🔹 Space Complexity: O(N)
    - Visited set stores up to `N` rooms.
    - Stack stores up to `N` rooms in the worst case.
--------------------------------------------------------------
"""

from typing import List

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set() 
        stack = [0]
        
        while stack:
            room = stack.pop() 
            visited.add(room)
            for key in rooms[room]:
                if key not in visited:
                    stack.append(key)
        
        return len(visited) == len(rooms)

# Example test case (Copy-paste & run)
rooms = [[1],[2],[3],[]]  # Expected output: True
solution = Solution()
print(solution.canVisitAllRooms(rooms))
