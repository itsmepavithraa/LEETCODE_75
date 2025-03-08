# 🚀 Asteroid Collision Problem

# 🧠 Problem Statement:
# You are given an array `asteroids` of integers representing asteroids in a row.  
# Each asteroid moves at the same speed.  
# - Positive value → Asteroid moves **right**.  
# - Negative value → Asteroid moves **left**.  

# When two asteroids collide:  
# - The smaller asteroid explodes.  
# - If they are the **same size**, both explode.  
# - Two asteroids moving in the **same direction never collide**.

# Return an array of **remaining asteroids** after all collisions.

# 🛠️ Example 1:
# Input: asteroids = [5, 10, -5]  
# Output: [5, 10]

# 🛠️ Example 2:
# Input: asteroids = [8, -8]  
# Output: []

# 🛠️ Example 3:
# Input: asteroids = [10, 2, -5]  
# Output: [10]

# ✅ Constraints:
# - `2 <= asteroids.length <= 10^4`
# - `-1000 <= asteroids[i] <= 1000`
# - `asteroids[i] ≠ 0`

# 🚀 Optimized Solution (Using Stack)

def asteroidCollision(asteroids):
    stack = []  # Stack to track surviving asteroids
    
    for asteroid in asteroids:
        # Check for collisions
        while stack and asteroid < 0 and stack[-1] > 0:
            if stack[-1] < -asteroid:   
                stack.pop()  # Right-moving asteroid explodes
                continue
            elif stack[-1] == -asteroid:  
                stack.pop()  # Both asteroids explode
            break
        
        else:
            stack.append(asteroid)  # No collision, add asteroid to stack
    
    return stack  # Return remaining asteroids

# 🚀 Example usage:
asteroids = [5, 10, -5]
print(asteroidCollision(asteroids))  # Output: [5, 10]

asteroids = [8, -8]
print(asteroidCollision(asteroids))  # Output: []

asteroids = [10, 2, -5]
print(asteroidCollision(asteroids))  # Output: [10]

asteroids = [-2, -1, 1, 2]
print(asteroidCollision(asteroids))  # Output: [-2, -1, 1, 2]

# 🕒 Time Complexity: O(N)  
# - **One pass through the array** + **O(1) stack operations** → Linear time.

# 🛢️ Space Complexity: O(N)  
# - **Stack space** to store surviving asteroids.


