'''
Part 1
Given a set of crops, each with a buy price (cost), sell price, and days to mature, along with a fixed budget, determine the set of crops to purchase that maximizes profit.

Input:
A list of crops, where each crop has:
    cost: The amount required to purchase the crop.
    sell_price: The amount received when selling the crop after maturity.
    day2mature: The number of days required for the crop to mature.
    An integer budget: The total money available for purchasing crops.

Output:
A list of crops to purchase that maximizes profit.
O(n x W)
'''


def knapsack_2d(costs,profit,W):
    n = len(costs)

    dp = []
    for i in range(n+1):
        temp = []
        for j in range(W+1):
            temp.append('0')
        dp.append(temp)
    


    for i in range(1,n+1):
        for w in range(1,W+1):
            if costs[i-1]<=w:
                dp[i][w] = max(dp[i-1][w], profit[i-1]+dp[i-1][w-costs[i-1]])
            
            else:
                dp[i][w]= dp[i-1][w]
    
    return dp[n][w]


