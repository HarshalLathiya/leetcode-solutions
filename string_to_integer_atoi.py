
# LeetCode 8: String to Integer (atoi)


class Solution:
    def myAtoi(self, s: str) -> int:
        INT_MAX = 2**31 - 1
        INT_MIN = -(2**31)

        i = 0
        n = len(s)

        # Skip leading spaces.
        while i < n and s[i] == ' ':
            i += 1

        # Determine sign.
        sign = 1

        if i < n and s[i] in ('+', '-'):
            if s[i] == '-':
                sign = -1
            i += 1

        limit = INT_MAX if sign == 1 else abs(INT_MIN)
        num = 0

        # Convert consecutive digits manually.
        while i < n and '0' <= s[i] <= '9':
            digit = ord(s[i]) - ord('0')

            # Prevent overflow.
            if num > limit // 10:
                return INT_MAX if sign == 1 else INT_MIN

            if num == limit // 10 and digit > limit % 10:
                return INT_MAX if sign == 1 else INT_MIN

            num = num * 10 + digit
            i += 1

        return sign * num


def main():
    solution = Solution()

    test_cases = [
        "42",
        " -042",
        "1337c0d3",
        "0-1",
        "words and 987",
        "+-12",
        "",
        "2147483648",
        "-2147483649",
        "00000000000123",
        "   +0",
        "   ",
    ]

    for s in test_cases:
        result = solution.myAtoi(s)
        print(f"Input: {s!r:24} Output: {result}")


if __name__ == "__main__":
    main()
