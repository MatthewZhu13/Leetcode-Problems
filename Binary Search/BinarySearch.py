class Solution(object):
    def search(self, nums, target):
        #establish left and right boundaries
        l, r = 0, len(nums) - 1
        while l <= r:
            #establish middle boundary 
            m = (r + l) // 2

            #if target = middle, return middle index
            if target == nums[m]:
                return m

            #if target is below middle, set middle as right boundary
            elif target < nums[m]:
                r = m - 1

            #if target is above middle, set middle as left boundary  
            else:
                l = m + 1

        return -1

        
