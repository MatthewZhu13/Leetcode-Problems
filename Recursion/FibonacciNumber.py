class Solution(object):
    def fib(self, n, dict = {}):
        #General apporach:
        #Work backwards from the end of the sequence at the nth place to try and get back to the beginning
        #Use memoization to save time complexity

        #Memoization to see if we have encountered this n before so we do nothave to run all the calculations of it again
        if (n in dict):
            return dict[n]

        #Base case that dictates when the recursion stops
        elif (n < 2):
            return n
        
        #storing each n we encounter and its result so we can reuse it again if we encounter it
        #fib (n-1) + fib(n-2) b/c fibonacci sequence is the product of the two numbers before it added togetehr
        dict[n] = self.fib(n-1, dict) + self.fib(n-2, dict)
        return dict[n]
        
