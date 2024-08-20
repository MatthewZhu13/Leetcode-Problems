import java.util.HashSet;
import java.util.Arrays;

class Solution {
    public boolean search(int[] nums, int target) {
        
        //binary search left and right pointers
        int left = 0;
        int right = nums.length - 1;

        while (left <= right){
            //middle variable
            int middle = left + (right - left) / 2;

            //for edgecases such as: [1, 0, 1, 1, 1]
            while ((left < middle) && (nums[left] == nums[middle])){
                left += 1;
            }
            
            //check if middle variable is equal to target or not
            if(nums[middle] == target){
                return true;
            }

            //check if left-middle is a sorted array
            else if(nums[left] <= nums[middle]){
                //check if target is between left-middle
                if ((nums[left] <= target) && (target < nums[middle])){
                    //if so move right to one under middle
                    right = middle - 1;
                }

                //otherwise move middle to one above middle
                else{
                    left = middle + 1;
                }

            }

            //otherwise middle-right is a sorted array
            else{
                //check if target is between middle-right
                if ((nums[middle] < target) && (target <= nums[right])){
                    //if so move left to one above middle
                    left = middle + 1;
                }

                else{
                    //otherwise move right to one under middle
                    right = middle - 1;
                }
            }
        }

        return false;
    }
}
