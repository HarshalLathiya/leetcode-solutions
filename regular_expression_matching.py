
# LeetCode 10: Regular Expression Matching


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)

        # dp[i][j] means s[:i] matches p[:j].
        dp = [[False] * (n + 1) for _ in range(m + 1)]

        # Empty string matches empty pattern.
        dp[0][0] = True

        # Initialize patterns that can match an empty string.
        for j in range(2, n + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 2]

        # Fill the DP table.
        for i in range(1, m + 1):
            for j in range(1, n + 1):

                # Ordinary character or wildcard '.'.
                if p[j - 1] == '.' or p[j - 1] == s[i - 1]:
                    dp[i][j] = dp[i - 1][j - 1]

                # '*' matches zero or more of the preceding element.
                elif p[j - 1] == '*':
                    # Option 1: Zero occurrences.
                    dp[i][j] = dp[i][j - 2]

                    # Option 2: One or more occurrences.
                    previous = p[j - 2]

                    if previous == '.' or previous == s[i - 1]:
                        dp[i][j] = (
                            dp[i][j] or dp[i - 1][j]
                        )

        return dp[m][n]


def main():
    solution = Solution()

    test_cases = [
        ("aa", "a", False),
        ("aa", "a*", True),
        ("ab", ".*", True),
        ("aab", "c*a*b", True),
        ("mississippi", "mis*is*p*.", False),
        ("", "a*", True),
        ("aaa", "a*a", True),
        ("ab", ".*c", False),
        ("abcd", "d*", False),
    ]

    for s, p, expected in test_cases:
        result = solution.isMatch(s, p)

        print(f"s        = {s!r}")
        print(f"p        = {p!r}")
        print(f"Result   = {result}")
        print(f"Expected = {expected}")
        print(f"Passed   = {result == expected}")
        print("-" * 40)


if __name__ == "__main__":
    main()
