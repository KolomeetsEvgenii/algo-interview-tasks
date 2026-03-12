"""
Contains Duplicate

Difficulty: easy
Tags: array, hashmap, set

Problem:
Дан массив целых чисел nums.
Нужно вернуть True, если какое-либо значение встречается в массиве
хотя бы два раза, и False — если все элементы различны.

Example 1:
Input: nums = [1, 2, 3, 1]
Output: True

Example 2:
Input: nums = [1, 2, 3, 4]
Output: False

Example 3:
Input: nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
Output: True

Idea:
1. Brute force:
   Сравниваем каждый элемент со всеми следующими.

2. Optimal:
   Храним уже просмотренные элементы в set.
   Если текущий элемент уже есть в set, значит найден дубликат.

Complexity:
Brute force:
Time: O(n^2)
Space: O(1)

Optimal:
Time: O(n)
Space: O(n)
"""


def contains_duplicate_bruteforce(nums: list[int]) -> bool:
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] == nums[j]:
                return True
    return False


def contains_duplicate(nums: list[int]) -> bool:
    seen = set()

    for num in nums:
        if num in seen:
            return True
        seen.add(num)

    return False


if __name__ == "__main__":
    print(contains_duplicate_bruteforce([1, 2, 3, 1]))  # True
    print(contains_duplicate([1, 2, 3, 1]))             # True
    print(contains_duplicate([1, 2, 3, 4]))             # False
    print(contains_duplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))  # True
