class Solution(object):
    def findMin(self, nums):
        #try to find the intersection point between the end of the rotated array and the start of the rotated array

        l, r = 0, len(nums) - 1
        while l < r:
            m = (l + r) // 2
            #if nums[middle] > nums[right], the minimum number must be on the right half of the array
            #do m + 1 as you can discount the current index you are on
            if nums[m] > nums[r]:
                l = m + 1

            #otherwise if nums[middle] < nums[right] the minimum index must be on the left half
            #don't do m + 1 as the current index you are on can be the answer 
            else:
                r = m
        
        return nums[l]

