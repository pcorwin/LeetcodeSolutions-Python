# Best Time to Buy and Sell Stock II

#You are given an integer array prices where prices[i] is the price of a given stock on the ith day.
#On each day, you may decide to buy and/or sell the stock.
#You can only hold at most one share of the stock at any time.
#However, you can buy it then immediately sell it on the same day.
#Find and return the maximum profit you can achieve.

# Constraints:
#   1 <= prices.length <= 105
#   0 <= prices[i] <= 104

def maxProfit(prices):
    profit = 0
    for i in range(1, len(prices)):
        if prices[i] > prices[i - 1]:
            profit += prices[i] - prices[i - 1]
    return profit

def main():
    testcases = [
        [7, 1, 5, 3, 6, 4],
        [1, 2, 3, 4, 5],
        [7, 6, 4, 3, 1]
    ]
    for i in testcases:
        print(f'prices = {i}\noutput = {maxProfit(i)}\n')

main()
