class Solution(object):
    def isPalindrome(self, s):
        #Array containing all upper case and lower case letters and numbers
        characters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "n", "m", "o", "p", "q", "r", "s", "t", "u", "v", "w","x", "y", "z", 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
        
        #Left and right pointer
        left, right = 0, len(s) - 1

        while (left < right):
            #If left character is not a letter or number, move closer to middle
            if s[left] not in characters:
                left += 1
                continue

            #If right character is not a letter or number, move closer to middle           
            if s[right] not in characters:
                right -= 1
                continue
            
            #If left and right characters do not equal each other, it cannot be a palindrome
            if s[left].lower() != s[right].lower():
                return False

            #Increment left and right pointers
            left += 1
            right -= 1

        return True
