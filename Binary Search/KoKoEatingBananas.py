import math

class Solution(object):
    def process(self, speed, piles, h):
        num = 0
        #find out how many hours it takes Koko to eat all the bananas at current eating speed
        for i in piles: num += math.ceil(i / float(speed))
        return num

    def minEatingSpeed(self, piles, h):
        l, r = 1, max(piles)
        while l < r:
            m = (l + r) // 2
            #Koko is eating too slow
            if self.process(m, piles, h) > h:
                #Increase how fast Koko is eating
                l = m + 1
            
            #Koko is eating too fast or just fast enough
            else:
                #Keep decreasing m until Koko eat all the bananas in h hours at the slowest speed
                #Don't do m - 1 b/c m is a possible solution and you might want to consider it again
                r = m

        #return eating speed
        return l  

