"""
Given the array prices where prices[i] is the price of the ith item in a shop. There is a special discount for items in the shop, if you buy the ith item, then you will receive a discount equivalent to prices[j] where j is the minimum index such that j > i and prices[j] <= prices[i], otherwise, you will not receive any discount at all.

Return an array where the ith element is the final price you will pay for the ith item of the shop considering the special discount.

Example 1:
    Input: prices = [8,4,6,2,3]
    Output: [4,2,4,2,3]
    Explanation:
    For item 0 with price[0]=8 you will receive a discount equivalent to prices[1]=4, therefore, the final price you will pay is 8 - 4 = 4.
    For item 1 with price[1]=4 you will receive a discount equivalent to prices[3]=2, therefore, the final price you will pay is 4 - 2 = 2.
    For item 2 with price[2]=6 you will receive a discount equivalent to prices[3]=2, therefore, the final price you will pay is 6 - 2 = 4.
    For items 3 and 4 you will not receive any discount at all.

Example 2:
    Input: prices = [1,2,3,4,5]
    Output: [1,2,3,4,5]
    Explanation: In this case, for all items, you will not receive any discount at all.

Example 3:
    Input: prices = [10,1,1,6]
    Output: [9,0,1,6]

Constraints:
    1 <= prices.length <= 500
    1 <= prices[i] <= 10^3
"""

def finalPrices(prices):
    finnal_prices = list()
    for i in range(len(prices)):
        discount = 0
        for j in range(i + 1, len(prices)):
            if prices[j] <= prices[i]:
                discount = prices[j]
                break
        finnal_prices.append(prices[i] - discount)
    return finnal_prices

prices = [8,4,6,2,3]
print(finalPrices(prices))

prices = [1, 2, 3, 4, 5]
print(finalPrices(prices))

prices = [10,1,1,6]
print(finalPrices(prices))



# 分数线 93。58
print(sum([30, 10, 37]))
# 1 合法稳定就业指标
    # 五险缴纳年限 * 3
# 2 合法稳定住所指标
    # 自有住房居住年限 * 1
    # 租房年限 * 0.5
# 3 教育背景指标
    # 本科 15
    # 硕士 26
# 4 职住区域指标

# 5 创新创业指标

# 6 纳税指标

