class Solution(object):
    def productExceptSelf(self, nums):
        """
        Approach: 
        1. Each integer in the array should be replaced by a product of all integers on the left and right of it
        2. Create a new array of all 1's
        3. Find all left side products and store that in the new array
        4. Find all right side products and replace the values in the original array with the product values
        4. Multiply each right side product with the respective left side product in the new array
        """

        #New array to store left side product values
        arr = [1] * len(nums)
        
        #Have first value stay as 1 as there are no more values on the left to multiply by
        for i in range(1, len(nums)):
            #Store the previous left product value in arr[i - 1] so you can just multiply that value by nums[i - 1] instead of recalculating it every time
            arr[i] = arr[i-1] * nums[i - 1]

        #Calculating the right product values and multiplying them by the left ones all in 1 step
        #Start at len(nums) - 2 as the rightmost value has no more numbers on the right of it
        #End at -1 so that that last value of j can be 0
        for j in range(len(nums) - 2, -1, -1):
            #Multiply arr[j] by the product of all ints on the right of it
            arr[j] = arr[j] * nums[j + 1]
            
            #Update nums[j] so that it is the product of values on the right of it so that we do not have to recalculate the product every time
            nums[j] = nums[j + 1] * nums[j]

        #Output statement
        return arr
