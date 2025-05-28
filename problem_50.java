/*
Question:
Implement a class called `SmallestInfiniteSet` that simulates an infinite set of positive integers starting from 1.

The class should support the following operations:

1. `popSmallest()`: Removes and returns the smallest number in the set.
2. `addBack(num)`: Adds a previously removed number back into the set. If the number is already present, do nothing.

Example:
SmallestInfiniteSet obj = new SmallestInfiniteSet();
System.out.println(obj.popSmallest());  // Output: 1
System.out.println(obj.popSmallest());  // Output: 2
obj.addBack(1);                         // Add 1 back to the set
System.out.println(obj.popSmallest());  // Output: 1
System.out.println(obj.popSmallest());  // Output: 3
System.out.println(obj.popSmallest());  // Output: 4

Constraints:
- 1 <= num <= 1000
- At most 1000 calls will be made to popSmallest and addBack.
*/

import java.util.HashSet;
import java.util.Set;

public class problem_50 {

    static class SmallestInfiniteSet {
        private int smallest;
        private Set<Integer> removed;

        public SmallestInfiniteSet() {
            smallest = 1;
            removed = new HashSet<>();
        }

        public int popSmallest() {
            int ret = smallest;
            removed.add(ret);
            smallest++;

            while (removed.contains(smallest)) {
                smallest++;
            }

            return ret;
        }

        public void addBack(int num) {
            if (removed.contains(num)) {
                removed.remove(num);
                if (num < smallest) {
                    smallest = num;
                }
            }
        }
    }

    // Example usage
    public static void main(String[] args) {
        SmallestInfiniteSet obj = new SmallestInfiniteSet();
        System.out.println(obj.popSmallest());  // Output: 1
        System.out.println(obj.popSmallest());  // Output: 2
        obj.addBack(1);                         // Add 1 back
        System.out.println(obj.popSmallest());  // Output: 1
        System.out.println(obj.popSmallest());  // Output: 3
        System.out.println(obj.popSmallest());  // Output: 4
    }
}

/*
Time Complexity:
- popSmallest(): O(1) on average, worst-case O(n) when skipping already removed numbers.
- addBack(num): O(1)

Space Complexity:
- O(n), where n is the number of removed numbers (up to 1000).
*/
