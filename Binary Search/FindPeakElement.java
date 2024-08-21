class Solution {
    public int findPeakElement(int[] nums) {
        //partition the array into parts that you know will have a peak
        //if middle < middle + 1, there is a guaranteed peak as middle - right can either keep going up consistently (peak is at end) or it will dip once (peak is before dip)
        //instead of partitioning the array based off of value size partition the array based off of if middle is smaller than the value on its left or right
        
        if (nums.length == 1){
            return 0;
        }

        int left = 0;
        int right = nums.length - 1;
        while (left <= right){
            int middle = left + (right - left);
            //if midddle is at the very start of the array
            if (middle == 0){
                //only check if middle is greater than right number
                if (nums[middle] > nums[middle + 1]){
                    return middle;
                }

                //if not then move left pointer to one past middle 
                //peak has to be on the right of middle as the right of pointer is going up
                else if (nums[middle] < nums[middle + 1]){
                    left = middle + 1;
                }
            }

            //if middle is at the very end of the array
            else if (middle == nums.length - 1){
                //only check if middle is greater than one before middle
                if (nums[middle] > nums[middle - 1]){
                    return middle;
                }

                //otherwise move right to one below middle
                //peak has to be on the left of middle as the left of pointer is going up
                else if (nums[middle] < nums[middle - 1]){
                    right = middle - 1;
                }
            }

            //check if middle is peak
            else if ((nums[middle - 1] < nums[middle]) && (nums[middle] > nums[middle + 1])){
                return middle;
            }

            //check if right of middle is larger than middle
            else if (nums[middle] < nums[middle + 1]){
                //peak has to be one past middle as the right of the pointer is going up
                left = middle + 1;
            } 

            //check if the middle is smaller than one before middle
            else if (nums[middle] < nums[middle - 1]){
                //peak has to be one before middle as the left of the pointer is going up
                right = middle - 1;
            }
        }

        return left;
    }
}
