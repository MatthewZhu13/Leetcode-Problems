class Solution(object):
    def longestConsecutive(self, nums):
        #Removes all duplicates from num + turns nums into a hashset
        nums = set(nums)
        maxSequence = 0


        for i in nums:
            #When you start counting the length of each subsequence, you need to start from the lowest value in that subsequence
            if (i - 1) not in nums:
                j = i + 1
                while j in nums:
                    #Keep incrementing j until you find the largest value in the subsequence
                    j += 1
                #Compare the length of each subsequence to the largest subsequence found already
                maxSequence = max(j - i, maxSequence)

        return maxSequence

        

        
