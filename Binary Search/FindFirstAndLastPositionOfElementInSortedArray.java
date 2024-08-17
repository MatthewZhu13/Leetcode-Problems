class Solution {
    public int[] searchRange(int[] nums, int target) {
        int[] ans = {-1, -1};
        int leftIdx = -1;
        int rightIdx = -1;

        int left = 0;
        int right = nums.length - 1;

        //binary search to find leftmost target value
        while (left <= right){
            int middle = left + (right - left) / 2;
            //once target value is found, store current index and move right bound to one under current index until you find the smallest index for the target
            if (nums[middle] == target){
                leftIdx = middle;
                right = middle - 1;
            }

            else if (nums[middle] < target){
                left = middle + 1;
            }

            else{
                right = middle - 1;
            }
        }
        ans[0] = leftIdx;

        //binary search to find rightmost target value
        left = 0;
        right = nums.length - 1;
        while (left <= right){
            int middle = left + (right - left) / 2;

            //once you find the target index, shift left index to 1 above target index until you find the rightmost target index
            if (nums[middle] == target){
                rightIdx = middle;
                left = middle + 1;
            }

            else if (nums[middle] < target){
                left = middle + 1;
            }

            else{
                right = middle - 1;
            }
        }
        ans[1] = rightIdx;
        return ans;
    } 
}
