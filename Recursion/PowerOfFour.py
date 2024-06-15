def powerOfFour(self, n, x = 1):
  #If constant x is ever > 4 and has not = 4 yet, then it is not a power of 4 
  if x > n:
    return False

  #Base case to stop the recursive cycle
  if n == x:
      return True

  #Recursive statement increasing constant x until it etiher equals or is > 4
  return self.powerOfFour(n, x * 4)
