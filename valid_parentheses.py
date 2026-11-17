class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        pairs = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        for char in s:

            # If it is an opening bracket,
            # push it onto the stack.
            if char in '([{':
                stack.append(char)

            # If it is a closing bracket,
            # check whether it matches the top.
            else:
                if not stack or stack[-1] != pairs[char]:
                    return False

                # Remove the matched opening bracket.
                stack.pop()

        # Valid only if all opening brackets were closed.
        return len(stack) == 0


def main():
    solution = Solution()

    test_cases = [
        ("()", True),
        ("()[]{}", True),
        ("(]", False),
        ("([])", True),
        ("([)]", False),
        ("{[]}", True),
        ("(((", False),
        ("))", False),
        ("", True),
        ("({[]})", True),
        ("(([]){})", True),
        ("[", False),
        ("([]{})", True),
    ]

    print("Valid Parentheses - Test Results")
    print("-" * 50)

    for index, (s, expected) in enumerate(test_cases, start=1):
        actual = solution.isValid(s)

        status = "PASS" if actual == expected else "FAIL"

        print(f"Test Case {index}: {status}")
        print(f"Input:    {s}")
        print(f"Expected: {expected}")
        print(f"Actual:   {actual}")
        print("-" * 50)


if __name__ == "__main__":
    main()