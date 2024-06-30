class Solution(object):
    def groupAnagrams(self, strs):
        
        #Create a dictionary to store each unique sorted anagram and the words that make up that anagram
        # dict = {
        #        |--- tea
        #   aet: |--- ate
        #        |--- eat
        #}
        dict = {}
        for i in range (len(strs)):
            #sort each element of strs to see its base sorted characters
            x = ''.join(sorted(strs[i]))
            #if that sorted character composition is in dict already, add the origianl word to array associated with the character composition
            if x in dict:
                dict[x].append(strs[i])
            
            #if it is not already in dict then add it in associated with an array with the original word in it
            else:
                dict[x] = [strs[i]]

        #Return all the values in the dictionary
        return dict.values()
