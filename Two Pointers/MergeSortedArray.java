import java.util.Arrays;

class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        //start from the end and compare the last elements of nums1 and nums2
        //fill in the greater value until you reach the end of either nums1 or nums2
        //if there are still values left in nums2 (n > 0), fill in the front couple indicies from 0-n with the remaining values 
        //you don't have to do the same with nums1 as the front is already prefilled with values

        while ((m > 0) && (n > 0)){
            if (nums1[m - 1] >= nums2[n - 1]){
                nums1[m + n - 1] = nums1[m - 1];
                m -= 1;
            }

            else{
                nums1[m + n - 1] = nums2[n - 1];
                n -= 1;
            }
        } 

        //check if nums2 has any numbers left to add into nums1
        while(n > 0){
            nums1[n - 1] = nums2[n - 1];
            n -= 1;
        }
    }
}
