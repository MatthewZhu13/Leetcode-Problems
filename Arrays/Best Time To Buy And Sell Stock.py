class Solution(object):
    def maxProfit(self, prices):

        #If there is only 1 listing of prices then you cannot make profit
        if len(prices) == 1:
            return 0

        #Initial buying price
        min_price = prices[0]
        profit = 0

        
        for i in range(1, len(prices)):
            #Constantly compare the smallest buying price found previously to the current stock price
            if prices[i] - min_price > profit:
                profit = prices[i] - min_price

            #Constantly compare the current price to the smallest stock price you have seen so far and update it with the smallest price
            elif prices[i] < min_price:
                min_price = prices[i]

        return profit
