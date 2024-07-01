class Solution:
    def encode(self, strs: List[str]) -> str:  
        string = "" 
        for i in range(len(strs)):
            #length of each word
            x = len(strs[i])

            #length of integer representation of the length of each word
            y = len(str(x))

            #add x to the beginning of the word to show how many characters long the word is
            #add y in front of x so you know how many indexes x takes up in case the length of the word is > 9
            string += str(y)
            string += str(x) 
            string += strs[i]
        
        return string

    def decode(self, s: str) -> List[str]:
        arr = []
        count = 0
        i = 0

        while i < len(s):
            #obtain the length of the length of each word
            count = int(s[i])
            #obtain the length of each word using slicing
            length = int(s[i + 1: i + 1 + count])
            #add each word to arr using slicing from i + 1 + count to i + 1 + count + length (not including)
            arr.append(s[i + 1 + count : i + 1 + count + length])
            #increment your index position
            i += (count + length + 1)
            
        
        return arr
