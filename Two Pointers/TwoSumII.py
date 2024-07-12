class Solution(object):
    def twoSum(self, numbers, target):
        #Have 2 pointers, one on the very left of numbers and one of the very right of numbers
        left, right = 0, len(numbers) - 1
        while left < right:
            #If left and right pointers equal each other then return indicies
            if numbers[left] + numbers[right] == target:
                return [left + 1, right + 1]
            
            #If left + right < target, move up left pointer as right is already as big as it can be since the array is sorted
            elif numbers[left] + numbers[right] < target:
                left += 1
            #If left + right > target, move down right pointer as left is already as smal as it can be since the array is sorted
            else:
                right -= 1
            

        
