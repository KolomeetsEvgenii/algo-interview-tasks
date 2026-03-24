"""
Best Time to Buy and Sell Stock

Difficulty: easy
Tags: array, greedy

Problem:
Дан массив prices, где prices[i] — цена акции в i-й день.

Нужно выбрать один день для покупки акции и другой день в будущем для продажи,
чтобы получить максимальную прибыль.

Верни максимальную прибыль, которую можно получить.
Если прибыль получить нельзя, верни 0.

Example 1:
Input: prices = [7, 1, 5, 3, 6, 4]
Output: 5

Explanation:
Buy on day 2 (price = 1) and sell on day 5 (price = 6),
profit = 6 - 1 = 5.

Example 2:
Input: prices = [7, 6, 4, 3, 1]
Output: 0

Idea:
1. Brute force:
   Проверяем все пары дней:
   для каждого дня покупки смотрим все возможные дни продажи после него.

2. Optimal:
   Идём по массиву слева направо.
   Храним минимальную цену, которую видели раньше.
   Для каждой текущей цены считаем прибыль, если продать сегодня.
   Обновляем максимальную прибыль.

Complexity:
Brute force:
Time: O(n^2)
Space: O(1)

Optimal:
Time: O(n)
Space: O(1)
"""


def max_profit_bruteforce(prices: list[int]) -> int:
    max_profit = 0

    for i in range(len(prices)):
        for j in range(i + 1, len(prices)):
            profit = prices[j] - prices[i]
            if profit > max_profit:
                max_profit = profit

    return max_profit


def max_profit(prices: list[int]) -> int:
    min_price = prices[0]
    max_profit = 0

    for price in prices:
        if price < min_price:
            min_price = price
        else:
            profit = price - min_price
            if profit > max_profit:
                max_profit = profit

    return max_profit


if __name__ == "__main__":
    print(max_profit_bruteforce([7, 1, 5, 3, 6, 4]))  # 5
    print(max_profit([7, 1, 5, 3, 6, 4]))             # 5
    print(max_profit([7, 6, 4, 3, 1]))                # 0
