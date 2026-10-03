"""Stack-based validator for balanced parentheses, brackets, and braces.

Uses last-in, first-out (LIFO) matching: the most recently opened bracket
must be the next one closed.
"""


def is_valid_parentheses(s: str) -> bool:
    """Return True if the brackets in ``s`` are balanced, otherwise False.

    Only ``()``, ``{}``, and ``[]`` are treated as brackets. Other
    characters are ignored.

    Approach:
        Walk the string once. Push each opening bracket onto a list used
        as a stack. A closing bracket must match the most recent unmatched
        opener. A dict maps each closer to its opener. If a closer arrives
        while the stack is empty, or the opener on top is the wrong one,
        the string is invalid. After the scan, leftover openers mean the
        string is still unbalanced.

    Complexity:
        O(n) time and O(n) space, where n is the length of ``s``.
    """
    stack = []
    closing_to_opening = {")": "(", "]": "[", "}": "{"}
    opening = set(closing_to_opening.values())

    # LIFO: the most recent opener must close first.
    for char in s:
        if char in opening:
            stack.append(char)
        elif char in closing_to_opening:
            if not stack or stack.pop() != closing_to_opening[char]:
                return False

    return len(stack) == 0


if __name__ == "__main__":
    samples = ["()", "{[()]}", "([]{})", "(", "([)]", "(()"]
    for sample in samples:
        label = "valid" if is_valid_parentheses(sample) else "invalid"
        print(f"{sample} -> {label}")
