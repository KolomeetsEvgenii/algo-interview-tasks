"""
Valid Parentheses

Difficulty: easy
Tags: stack, string

Problem:
Дана строка s, состоящая только из символов:
'(', ')', '{', '}', '[' и ']'.

Нужно вернуть True, если строка является корректной,
и False — в противном случае.

Строка считается корректной, если:
1. Каждая открывающая скобка закрывается скобкой того же типа.
2. Открывающие скобки закрываются в правильном порядке.
3. Каждая закрывающая скобка имеет соответствующую открывающую.

Example 1:
Input: s = "()"
Output: True

Example 2:
Input: s = "()[]{}"
Output: True

Example 3:
Input: s = "(]"
Output: False

Example 4:
Input: s = "([)]"
Output: False

Example 5:
Input: s = "{[]}"
Output: True

Idea:
Используем stack.
- Если встречаем открывающую скобку, кладём её в стек.
- Если встречаем закрывающую, проверяем верхушку стека.
- Если стек пустой или тип скобок не совпадает, возвращаем False.
- В конце стек должен быть пустым.

Complexity:
Time: O(n)
Space: O(n)
"""


def valid_parentheses(s: str) -> bool:
    stack = []
    pairs = {
        ')': '(',
        ']': '[',
        '}': '{'
    }

    for ch in s:
        if ch in '([{':
            stack.append(ch)
        else:
            if not stack:
                return False
            top = stack.pop()
            if top != pairs[ch]:
                return False

    return len(stack) == 0


if __name__ == "__main__":
    print(valid_parentheses("()"))      # True
    print(valid_parentheses("()[]{}"))  # True
    print(valid_parentheses("(]"))      # False
    print(valid_parentheses("([)]"))    # False
    print(valid_parentheses("{[]}"))    # True
    print(valid_parentheses("((("))     # False
