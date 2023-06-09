#Best Time to Buy and Sell Stock

#You are given an array prices where prices[i] is the price of a given stock on the ith day.
#You want to maximize your profit by choosing a single day to buy one stock and choosing a different
#   day in the future to sell that stock.
#Return the maximum profit you can achieve from this transaction.
#If you cannot achieve any profit, return 0.

#Constraints:
#   1 <= prices.length <= 105
#   0 <= prices[i] <= 104

def maxProfit(prices):
    profit = 0
    l = 0
    for r in range(1, len(prices)):
        if prices[r ] >prices[l]:
            profit = max(profit, prices[r] -prices[l])
        else:
            l = r
    return profit

def main():
    testcases = [
        [7, 1, 5, 3, 6, 4],
        [7, 6, 4, 3, 1]
    ]
    for i in testcases:
        print(f'prices = {i}\noutput = {maxProfit(i)}\n')

main()
