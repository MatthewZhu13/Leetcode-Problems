class Solution(object):
    def twoSum(self, nums, target):
        remainder = 0
        dict = {}

        for index, value in enumerate(nums):
            remainder = target - value
            if remainder in dict:
                return(index, dict[remainder])
            else:
                dict[value] = index
        
