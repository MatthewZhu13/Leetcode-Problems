import java.util.Arrays;
class Solution {
    public int threeSumClosest(int[] nums, int target) {
        //sort array so you can use left and right pointers
        Arrays.sort(nums);
        //base value to keep track of closest sum to target
        int num = nums[0] + nums[1] + nums[2];

        for(int i = 0; i < nums.length - 2; i++){
            //create left and right pointer for every i
            int left = i + 1;
            int right = nums.length - 1;
            while(left < right){
                int value = nums[i] + nums[left] + nums[right];

                //if i + left + right = target return that sum
                if (value == target){
                    return value;
                }

                //if i + left + right is closer to target than num, change num to i + left + right
                else if (Math.abs(value - target) <= Math.abs(num - target)){
                    num = value;
                }

                //if i + left + right is smaller than target, move left up one 
                if(value < target){
                    left += 1;
                }

                //if i + left + right is larger than target, move right down one 
                else if (value > target){
                    right -= 1;
                }
            }
        }
        return num;
    }
}
