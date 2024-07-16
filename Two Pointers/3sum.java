import java.util.Arrays;
import java.util.HashSet; 


class Solution {
    public List<List<Integer>> threeSum(int[] nums) {

        //Sort array
        Arrays.sort(nums);

        //Create set to avoid duplicate entries
        Set<List<Integer>> set = new HashSet<>();

        //Iterate through nums from the beginning to 2 before the end to ensure there is room for left and right pointers at the end of the for loop
        //For every i, create two pointers one starting at the start of the rest of the arr and one at the end of the rest of the arr (left, right)
        //If i + left + right = 0, add to the set
        //If i + left + right < 0, move left up 1 as nums is sorted
        //If i + left + right > 0, move right down 1 as nums is sorted

        for (int i = 0; i < nums.length - 2; i++){
            int left = i + 1;
            int right = nums.length - 1;

            while (left < right){
                int total = nums[i] + nums[left] + nums[right];
                if (total == 0){
                    ArrayList<Integer> insert = new ArrayList<>();
                    insert.add(nums[i]);
                    insert.add(nums[left]);
                    insert.add(nums[right]);
                    set.add(insert);
                    left += 1;
                }

                else if (total > 0){
                    right -= 1;
                }
                
                else{
                    left += 1;
                }
            }
        }

        return new ArrayList<>(set);
    }
}
