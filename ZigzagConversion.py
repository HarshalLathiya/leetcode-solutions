# LeetCode 6: Zigzag Conversion

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # No zigzag movement is needed in these cases.
        if numRows == 1 or numRows >= len(s):
            return s

        # Create one row for each zigzag row.
        rows = [""] * numRows

        current_row = 0
        direction = 1  # 1 = down, -1 = up

        for char in s:
            rows[current_row] += char

            # Change direction at the top and bottom rows.
            if current_row == 0:
                direction = 1
            elif current_row == numRows - 1:
                direction = -1

            current_row += direction

        # Read the rows from top to bottom.
        return "".join(rows)


def main():
    solution = Solution()

    # Example 1
    s = "PAYPALISHIRING"
    numRows = 3
    print("Example 1:", solution.convert(s, numRows))

    # Example 2
    s = "PAYPALISHIRING"
    numRows = 4
    print("Example 2:", solution.convert(s, numRows))

    # Example 3
    s = "A"
    numRows = 1
    print("Example 3:", solution.convert(s, numRows))

    # Additional test cases
    print("Extra test 1:", solution.convert("AB", 1))
    print("Extra test 2:", solution.convert("ABCDE", 5))
    print("Extra test 3:", solution.convert("ABCDE", 2))


if __name__ == "__main__":
    main()
