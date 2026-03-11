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
"""


def two_sum(nums: list[int], target: int) -> list[int]:
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [nums[i], nums[j]]
    return []


def two_sum1(nums: list[int], target: int) -> list[int]:
    seen = {}
    for i in range(len(nums)):
        need = target - nums[i]
        if need in seen:
            return [seen[need], i]
        seen[nums[i]] = i
    return []


if __name__ == "__main__":
    print(two_sum([2, 7, 11, 15], 9))
