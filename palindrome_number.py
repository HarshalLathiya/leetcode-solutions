# LeetCode 9: Palindrome Number

class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Negative numbers cannot be palindromes.
        if x < 0:
            return False

        # A non-zero number ending in zero cannot be a palindrome.
        if x != 0 and x % 10 == 0:
            return False

        reversed_half = 0

        # Reverse only the last half of the digits.
        while x > reversed_half:
            digit = x % 10
            reversed_half = reversed_half * 10 + digit
            x //= 10

        # Handle even- and odd-length numbers.
        return (
            x == reversed_half
            or x == reversed_half // 10
        )


def main():
    solution = Solution()

    test_cases = [
        121,
        -121,
        10,
        0,
        1221,
        12321,
        123,
        1001,
        123454321,
        2147483647,
    ]

    for x in test_cases:
        result = solution.isPalindrome(x)
        print(f"Input: {x:>12}  Output: {result}")


if __name__ == "__main__":
    main()
