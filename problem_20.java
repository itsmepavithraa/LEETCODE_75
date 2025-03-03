// Question: Find the Difference of Two Arrays
// 
// You are given two integer arrays `nums1` and `nums2`. 
// The task is to return a list of two lists:
// - The first list contains elements that are in `nums1` but not in `nums2`.
// - The second list contains elements that are in `nums2` but not in `nums1`.
// 
// Each element in the result must be unique, and you may return the result in any order.
// 
// Example:
// Input: nums1 = [1, 2, 3], nums2 = [2, 4, 6]
// Output: [[1, 3], [4, 6]]

import java.util.*;

public class problem_20 {

    // Approach 1: Using Loop and Manual Check
    public static List<List<Integer>> findDifferenceManual(int[] nums1, int[] nums2) {
        Set<Integer> set1 = new HashSet<>();
        Set<Integer> set2 = new HashSet<>();
        
        for (int num : nums1) set1.add(num);
        for (int num : nums2) set2.add(num);
        
        List<Integer> ans1 = new ArrayList<>();
        for (int num : set1) {
            if (!set2.contains(num)) {
                ans1.add(num);
            } else {
                set2.remove(num);
            }
        }
        
        return Arrays.asList(ans1, new ArrayList<>(set2));
    }

    // Approach 2: Using Set Operations
    public static List<List<Integer>> findDifferenceSet(int[] nums1, int[] nums2) {
        Set<Integer> set1 = new HashSet<>();
        Set<Integer> set2 = new HashSet<>();
        
        for (int num : nums1) set1.add(num);
        for (int num : nums2) set2.add(num);
        
        List<Integer> diff1 = new ArrayList<>(set1);
        diff1.removeAll(set2);
        
        List<Integer> diff2 = new ArrayList<>(set2);
        diff2.removeAll(set1);
        
        return Arrays.asList(diff1, diff2);
    }

    public static void main(String[] args) {
        int[] nums1 = {1, 2, 3};
        int[] nums2 = {2, 4, 6};
        
        // Test both approaches
        System.out.println("Approach 1 (Manual Check) Result: " + findDifferenceManual(nums1, nums2));
        System.out.println("Approach 2 (Set Operations) Result: " + findDifferenceSet(nums1, nums2));
    }
}

// Time Complexity: O(m + n)
// Space Complexity: O(m + n)

// Let me know if you’d like me to tweak the code or add explanations! 🚀
