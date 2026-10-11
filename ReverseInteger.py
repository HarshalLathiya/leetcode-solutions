
# LeetCode: Reverse Integer

class Solution:
    def reverse(self, x: int) -> int:
        INT_MAX = 2**31 - 1
        INT_MIN = -(2**31)

        sign = -1 if x < 0 else 1
        x = abs(x)

        # Negative integers can have one extra unit of magnitude.
        limit = INT_MAX if sign == 1 else abs(INT_MIN)

        reversed_num = 0

        while x > 0:
            digit = x % 10
            x //= 10

            # Prevent overflow before appending the digit.
            if reversed_num > limit // 10:
                return 0

            if (
                reversed_num == limit // 10
                and digit > limit % 10
            ):
                return 0

            reversed_num = reversed_num * 10 + digit

        return sign * reversed_num


def main():
    solution = Solution()

    test_cases = [
        123,
        -123,
        120,
        0,
        1534236469,
        -2147483648,
        1463847412,
    ]

    for x in test_cases:
        result = solution.reverse(x)
        print(f"Input: {x:>12}  Output: {result}")


if __name__ == "__main__":
    main()
