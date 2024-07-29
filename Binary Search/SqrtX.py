class Solution(object):
    def mySqrt(self, x):
        #Create left and right variables
        l, r = 0, x

        #Binary search
        while l <= r:
            #Calculate middle variable
            m = (l + r) // 2

            #mOver is for if the answer is a float
            mOver = m + 1

            if m * m == x:
                return m
            
            #Check if answer is between m and mOver (determines if the answer is a float)
            elif m * m < x and mOver * mOver > x:
                #if answer is a float, return rounded down version of the float (m)
                return m
            
            #If m * m is > target, move the right variable down since m is too big
            elif m * m > x:
                r = m - 1

            #If m * m is < target, move the left variable up since m is too small
            else:
                l = m + 1
            
        return -1
        
