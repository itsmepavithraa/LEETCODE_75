// LeetCode 75: Find Pivot Index (Java Solution)

/*
🧠 Problem Statement:
Given an array of integers `nums`, find the pivot index.  
The pivot index is the index where the sum of all elements to the left is equal to the sum of all elements to the right.  

Return the leftmost pivot index. If no such index exists, return -1.

🔑 Example:
Input: nums = [1, 7, 3, 6, 5, 6]  
Output: 3  
Explanation:  
- Left sum: 1 + 7 + 3 = 11  
- Right sum: 5 + 6 = 11  

📘 Constraints:  
- 1 <= nums.length <= 10^4  
- -1000 <= nums[i] <= 1000  
*/

public class problem_19 {
    public int pivotIndex(int[] nums) {
        int leftSum = 0;
        int rightSum = 0;

        // Calculate the total sum of the array
        for (int num : nums) {
            rightSum += num;
        }

        // Iterate through the array
        for (int i = 0; i < nums.length; i++) {
            rightSum -= nums[i]; // Subtract the current element from right sum

            if (leftSum == rightSum) {
                return i; // Found the pivot index
            }

            leftSum += nums[i]; // Add the current element to the left sum
        }

        return -1; // No pivot index found
    }

    // 🛠️ Example Usage:
    public static void main(String[] args) {
        problem_19 solution = new problem_19();
        int[] nums = {1, 7, 3, 6, 5, 6};
        int result = solution.pivotIndex(nums);
        System.out.println("Pivot Index: " + result);
    }
}

/*
⚡ Time Complexity: O(N)  
- We traverse the array once, so the complexity is linear.

💾 Space Complexity: O(1)  
- Constant space is used for leftSum and rightSum.
*/
