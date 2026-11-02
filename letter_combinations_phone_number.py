
from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        if not digits:
            return []

        phone = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        result = []

        def backtrack(index, current):

            # Base condition
            if index == len(digits):
                result.append(current)
                return

            # Get letters for the current digit
            letters = phone[digits[index]]

            # Explore each letter
            for letter in letters:
                backtrack(index + 1, current + letter)

        backtrack(0, "")

        return result


def main():
    solution = Solution()

    test_cases = [
        ("23", [
            "ad", "ae", "af",
            "bd", "be", "bf",
            "cd", "ce", "cf"
        ]),

        ("2", ["a", "b", "c"]),

        ("79", [
            "pw", "px", "py", "pz",
            "qw", "qx", "qy", "qz",
            "rw", "rx", "ry", "rz",
            "sw", "sx", "sy", "sz"
        ]),

        ("234", None),

        ("", []),

        ("99", [
            "ww", "wx", "wy", "wz",
            "xw", "xx", "xy", "xz",
            "yw", "yx", "yy", "yz",
            "zw", "zx", "zy", "zz"
        ])
    ]

    print("Letter Combinations - Test Results")
    print("-" * 50)

    for index, (digits, expected) in enumerate(test_cases, start=1):

        result = solution.letterCombinations(digits)

        if expected is None:
            passed = len(result) == 27
        else:
            passed = sorted(result) == sorted(expected)

        status = "PASS" if passed else "FAIL"

        print(f"Test Case {index}: {status}")
        print(f"Input:    {digits}")
        print(f"Output:   {result}")
        print(f"Count:    {len(result)}")
        print("-" * 50)


if __name__ == "__main__":
    main()
