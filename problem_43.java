/*
🔹 Problem: Keys and Rooms (LeetCode 841 - Medium)

You are given an array `rooms` where `rooms[i]` is a list of keys in room `i`. 
Each key unlocks another room. All rooms are locked initially, except for room `0`.  

Your task is to return `true` if you can visit all rooms, otherwise return `false`.  

### Example 1:
Input: rooms = [[1],[2],[3],[]]
Output: true
Explanation:  
- Start in room `0`, collect key `1`.  
- Go to room `1`, collect key `2`.  
- Go to room `2`, collect key `3`.  
- Go to room `3`, all rooms are visited.

### Example 2:
Input: rooms = [[1,3],[3,0,1],[2],[0]]
Output: false
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
*/

import java.util.*;

class problem_43 {
    public boolean canVisitAllRooms(List<List<Integer>> rooms) {
        Set<Integer> visited = new HashSet<>();
        Stack<Integer> stack = new Stack<>();
        stack.push(0); // Start from room 0

        while (!stack.isEmpty()) {
            int room = stack.pop();
            visited.add(room);
            for (int key : rooms.get(room)) {
                if (!visited.contains(key)) {
                    stack.push(key);
                }
            }
        }

        return visited.size() == rooms.size();
    }

    public static void main(String[] args) {
        // Example test case (Copy-paste & run)
        List<List<Integer>> rooms = new ArrayList<>();
        rooms.add(Arrays.asList(1));
        rooms.add(Arrays.asList(2));
        rooms.add(Arrays.asList(3));
        rooms.add(new ArrayList<>()); // Empty list for last room

        problem_43 solution = new problem_43();
        System.out.println(solution.canVisitAllRooms(rooms)); // Expected output: true
    }
}

