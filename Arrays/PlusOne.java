class Solution {
    public int[] plusOne(int[] digits) {
        for (int i = digits.length - 1; i >= 0; i--){
            if(digits[i] < 9){
                //if the last digit is < 9 then you just add 1 to the end and return digits
                digits[i] += 1;
                return digits;
            }
            //if the last digits is not < 9 then it has to be 9 so replace digits[i] with 0 and move to the next index to the left to increase that one as the sum will be 10 and the 1 carries over
            //if the next digit to the left is also = 9 then repeat the pattern
            digits[i] = 0;
        }

        //If the for loop completed without returning anything and you have gotten to here then that means that the whole array is full of 9s and you need to add a 1 to the front to make it complete
        //Create a new array full of zeros with a length 1 greater than digits previously
        digits = new int[digits.length + 1];
        //Make the first index = 1
        digits[0] = 1;
        return digits;

    }
}
