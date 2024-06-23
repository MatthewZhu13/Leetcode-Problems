class Solution(object):
    def climbStairs(self, n, dict = {}):
        
        if n == 1 or n == 2 or n == 3:
            return n

        if n in dict:
            return dict[n]

        else:
            dict[n] = self.climbStairs(n - 1, dict) + self.climbStairs(n - 2, dict)
            return dict[n]
        
