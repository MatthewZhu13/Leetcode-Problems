class Solution(object):
    def isPowerOfThree(self, n):
        #Base case + recursive base case
        #If n is negative or < 0 it is not a power of 3
        #If n = 1 then it is a power of 3
        if n <= 1:
            return n == 1
        
        #Check if n is divisible by 3 with no remainders
        if n % 3 == 0:
            #Recursively divide n by 3 until it becomes 3's simplest power (1)
            return self.isPowerOfThree(n / 3)
        
        #If n is not divisible by 3 with no remainders then it is not a power of 3
        return False
