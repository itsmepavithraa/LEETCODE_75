# Number of Recent Calls Problem

# Problem Statement:
# Design a class RecentCounter that counts recent requests within a sliding window of 3000 milliseconds.
# 
# Implement the following methods:
# - RecentCounter(): Initializes the counter.
# - ping(int t): Adds a new request at time t, and returns the number of requests 
#                that occurred in the time range [t - 3000, t], inclusive.

# Example:
# Input: ["RecentCounter", "ping", "ping", "ping", "ping"]
#        [[], [1], [100], [3001], [3002]]
# Output: [null, 1, 2, 3, 3]

# Explanation:
# ping(1) → 1 request in the last 3000 ms
# ping(100) → 2 requests in the last 3000 ms
# ping(3001) → 3 requests in the last 3000 ms
# ping(3002) → 3 requests in the last 3000 ms (request at 1 is removed)

from collections import deque

class RecentCounter:
    def __init__(self):
        self.q = deque()

    def ping(self, t: int) -> int:
        # Add the current timestamp to the queue
        self.q.append(t)
        
        # Remove timestamps older than 3000 milliseconds
        while self.q and self.q[0] < t - 3000:
            self.q.popleft()
        
        # Return the count of recent requests
        return len(self.q)

# Example usage:
if __name__ == "__main__":
    obj = RecentCounter()
    print(obj.ping(1))    # Output: 1
    print(obj.ping(100))  # Output: 2
    print(obj.ping(3001)) # Output: 3
    print(obj.ping(3002)) # Output: 3

# Time Complexity: O(1) (amortized)
# Space Complexity: O(N) where N is the number of requests in the last 3000 ms
