import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

public class No_1_Two_Sum {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Solution s = new Solution();
		int[] nums = {2, 7, 11, 15};
		int target = 9;
		int[] result = s.twoSum(nums, target);
		System.out.println(Arrays.toString(result));
	}

}

class Solution {
	public int[] twoSum(int[] nums, int target) {
		int[] result = null;
		for (int i = 0; i < nums.length; i++) {
			for (int j = i + 1; j< nums.length; j++) {
				if (nums[i] + nums[j] == target) {
					result = new int[] {i, j};
					break;
				}
			}
		}
		return result;
	}
}

/*
Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice

Example:
	Given nums = [2, 7, 11, 15], target = 9,
	Because nums[0] + nums[1] = 2 + 7 = 9,
	return [0, 1].
*/