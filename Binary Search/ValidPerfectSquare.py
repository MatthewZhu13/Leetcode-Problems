class Solution(object):
    def isPerfectSquare(self, num):
        #ordinary binary search but instead of comparing middle to num compare middle squared to num
        l, r = 0, num
        while l <= r:
            m = (l + r) // 2
            mSqr = m ** 2

            if mSqr == num:
                return True

            if mSqr > num:
                r = m - 1
            
            else:
                l = m + 1
        
        return False

        
