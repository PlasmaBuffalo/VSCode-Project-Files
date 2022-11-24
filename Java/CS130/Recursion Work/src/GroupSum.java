
public class GroupSum {
    public static void main(String[] args) {
        // create instance of main class
        GroupSum gs = new GroupSum();
        // test the groupSum method
        System.out.println(gs.groupSum(0, new int[] { 2, 4, 8 }, 10));
        System.out.println(gs.groupSum(0, new int[] { 2, 4, 8 }, 14));
        System.out.println(gs.groupSum(0, new int[] { 2, 4, 8 }, 9));
    }

    // method to determine if a group of numbers can add up to a given sum using
    // recursion
    public boolean groupSum(int start, int[] nums, int target) {
        // base case: if the target is 0, return true
        if (target == 0) {
            return true;
        }
        // base case: if the target is less than 0, return false
        if (target < 0) {
            return false;
        }
        // base case: if the start is greater than the length of the array, return false
        if (start >= nums.length) {
            return false;
        }
        // recursive case: if the target is greater than 0, call the method again with
        // the start incremented by 1 and the target subtracted by the value at the
        // start index
        return (groupSum(start + 1, nums, target - nums[start]) || groupSum(start + 1, nums, target));
    }
}

// cases:
// the target could be some number already in the add array
// the target could be a number that is not in the add array, but can be
// composed of numbers in the add array
// the target could be a number that is not in the add array and cannot be
// composed of numbers in the add array