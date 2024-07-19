class Solution(object):
    def maxArea(self, height):
        #Start with a pointer (left, right), one at start of array and one at end of array
        #Calculate the are between the left and right pointers
        #Move the pointer with the smallest height of the two as the smaller height does not support a large area of water
        left, right = 0, len(height) - 1
        maxArea = 0
        while left < right:
            area = (right - left) * min(height[left], height[right])
            if area > maxArea:
                maxArea = area
            
            if height[left] < height[right]:
                left += 1
            
            else:
                right -= 1
        
        return maxArea

        
