class Solution:

    def generateParenthesis(self, n):

        result = []

        def backtrack(current, open_count, close_count):

            # Base case
            if len(current) == 2 * n:
                result.append(current)
                return

            # Option 1: Add '('
            if open_count < n:
                backtrack(
                    current + "(",
                    open_count + 1,
                    close_count
                )

            # Option 2: Add ')'
            if close_count < open_count:
                backtrack(
                    current + ")",
                    open_count,
                    close_count + 1
                )

        # Start backtracking
        backtrack("", 0, 0)

        return result


def main():

    solution = Solution()

    # Test Case 1
    n = 3

    result = solution.generateParenthesis(n)

    print("Test Case 1")
    print("Input  :", n)
    print("Output :", result)
    print()

    # Test Case 2
    n = 1

    result = solution.generateParenthesis(n)

    print("Test Case 2")
    print("Input  :", n)
    print("Output :", result)
    print()

    # Additional Test Case
    n = 2

    result = solution.generateParenthesis(n)

    print("Test Case 3")
    print("Input  :", n)
    print("Output :", result)


if __name__ == "__main__":
    main()