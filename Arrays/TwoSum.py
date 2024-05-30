class Solution(object):
    def twoSum(self, nums, target):
        #Notes:
        #array problems ususally involve finding 2 indicies or values that equal a sum    

        
        #Variable that is: target - value you are currently
        #Determines what value you need to find in the array
        remainder = 0

        #Stores previously iterated over values and their indexes
        """dict = {
            7 : 0
            2 : 1
            4 : 2
        }
        """
        dict = {}

        for index, value in enumerate(nums):
            #Determines what value you need to find in the array
            remainder = target - value

            #Looks back in dict to see if you remainder is a value you have iterated over already in the array
            if remainder in dict:
                #Output statement
                return(index, dict[remainder])
            else:
                #If remainder is not in dict, store the current value and index in dict and move on
                dict[value] = index
        
