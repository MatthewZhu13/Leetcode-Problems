class Solution(object):
    def searchMatrix(self, matrix, target):

        #Use binary search to find what row target is in
        targetArr = []
        l, r = 0, len(matrix) - 1
        while l <= r:
            m = (l + r) // 2
            #If target is between the lower and upper bound of the row, then set that as the targetArr
            if matrix[m][0] <= target and target <= matrix[m][len(matrix[m]) - 1]:
                targetArr = matrix[m]
                break
            
            elif target < matrix[m][0]:
                r = m - 1
            
            else:
                l = m + 1

        #Perform a binary search on that row to find target
        l, r = 0, len(targetArr) - 1
        while l <= r:
            m = (l + r) // 2
            if targetArr[m] == target:
                return True

            elif targetArr[m] < target:
                l = m + 1
            
            else:
                r = m - 1

        #If target is not found, return False
        return False
        
        
