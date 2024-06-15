def powerOfFour(self, n, x = 1):
  #If constant x is ever > n and has not = n yet, then it is not a power of 3
  if x > n:
    return False

  #Base case to stop the recursive cycle
  if n == x:
      return True

  #Recursive statement increasing constant x until it etiher equals or is > n
  return self.powerOfFour(n, x * 4)
