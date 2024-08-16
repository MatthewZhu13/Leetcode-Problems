import math 
class Solution(object):
    def search(self, nums, target):
        #general ideas: since the array is rotated and easier way of thinking about it is as 2 seperate sorted arrays
        #through the binary search try and find the 2 sorted arrays and isolate the one that the target value is in and perform a binary search on that array

        #binary search left and right pointers
        l, r = 0, len(nums) - 1

        while l <= r:
            m = l + (r - l) // 2
            if nums[m] == target:
                return m
                
            #check if the array on the left of middle is a sorted array
            elif nums[l] <= nums[m]:
                #if target is between the left and middle, move right pointer to middle
                if nums[l] <= target and target <= nums[m]:
                    r = m

                #otherwise move left pointer to one past the middle pointer
                else:
                    l = m + 1

            #check if the array on the right of middle is sorted
            elif nums[m] <= nums[r]:
                #if target is in between middle and right pointers, move the left to the middle pointer
                if nums[m] <= target and target <= nums[r]:
                    l = m

                #otherwise move the right pointer to one below the middle pointer
                else:
                    r = m - 1        

        return -1
