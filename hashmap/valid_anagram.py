"""
Valid Anagram

Difficulty: easy
Tags: hashmap, string

Problem:
Даны две строки s и t.
Нужно вернуть True, если t является анаграммой s,
и False — в противном случае.

Анаграмма — это слово или фраза, полученная перестановкой букв другого слова,
с использованием всех исходных букв ровно один раз.

Example 1:
Input: s = "anagram", t = "nagaram"
Output: True

Example 2:
Input: s = "rat", t = "car"
Output: False

Idea:
1. Simple:
   Можно отсортировать обе строки и сравнить результат.

2. Optimal:
   Считаем, сколько раз каждый символ встречается в строке s.
   Затем проходим по строке t и уменьшаем соответствующие счётчики.
   Если символа нет или счётчик стал отрицательным, строки не являются
   анаграммами.

Complexity:
Simple:
Time: O(n log n)
Space: O(n)

Optimal:
Time: O(n)
Space: O(n)
"""


def valid_anagram_sort(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    return sorted(s) == sorted(t)


def valid_anagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    count = {}

    for ch in s:
        count[ch] = count.get(ch, 0) + 1

    for ch in t:
        if ch not in count:
            return False
        count[ch] -= 1
        if count[ch] < 0:
            return False

    return True


if __name__ == "__main__":
    print(valid_anagram_sort("anagram", "nagaram"))  # True
    print(valid_anagram("anagram", "nagaram"))       # True
    print(valid_anagram("rat", "car"))               # False
    print(valid_anagram("aab", "aba"))               # True
    print(valid_anagram("aab", "abb"))               # False
