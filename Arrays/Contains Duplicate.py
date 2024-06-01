class Solution(object):
    def containsDuplicate(self, nums):
        #A set only contains unique elements
        hash_set = set()

        for i in nums:
            #Since there are no duplicates in a set, if a element from the array is already in the set, it is a duplicate
            if i in hash_set:
                return True
            
            #Iterate through nums and add each element to the set
            hash_set.add(i)

        return False
