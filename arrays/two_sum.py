"""
Two Sum

Difficulty: easy
Tags: array, hashmap

Problem:
Дан массив целых чисел nums и целое число target.
Нужно вернуть индексы двух чисел так, чтобы их сумма была равна target.

Предполагается, что ровно одно решение существует,
и один и тот же элемент нельзя использовать дважды.

Можно вернуть ответ в любом порядке.

Example 1:
Input: nums = [2, 7, 11, 15], target = 9
Output: [0, 1]

Example 2:
Input: nums = [3, 2, 4], target = 6
Output: [1, 2]

Example 3:
Input: nums = [3, 3], target = 6
Output: [0, 1]

Idea:
1. Brute force:
   Проверяем все пары чисел двумя вложенными циклами.

2. Optimal:
   Храним уже просмотренные числа в словаре:
   число -> индекс.
   Для текущего числа ищем target - num.

Complexity:
Brute force:
Time: O(n^2)
Space: O(1)

Optimal:
Time: O(n)
Space: O(n)
"""


def two_sum_bruteforce(nums: list[int], target: int) -> list[int]:
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []


def two_sum(nums: list[int], target: int) -> list[int]:
    seen = {}

    for i, num in enumerate(nums):
        need = target - num
        if need in seen:
            return [seen[need], i]
        seen[num] = i

    return []


if __name__ == "__main__":
    print(two_sum_bruteforce([2, 7, 11, 15], 9))  # [0, 1]
    print(two_sum([2, 7, 11, 15], 9))             # [0, 1]
    print(two_sum([3, 2, 4], 6))                  # [1, 2]
    print(two_sum([3, 3], 6))                     # [0, 1]
