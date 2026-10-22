
class Solution:
    def intToRoman(self, num: int) -> str:
        values = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4, 1
        ]

        symbols = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV", "I"
        ]

        result = []

        for value, symbol in zip(values, symbols):
            while num >= value:
                result.append(symbol)
                num -= value

        return "".join(result)


def main():
    solution = Solution()

    test_cases = [
        (3749, "MMMDCCXLIX"),
        (58, "LVIII"),
        (1994, "MCMXCIV"),
        (4, "IV"),
        (9, "IX"),
        (40, "XL"),
        (90, "XC"),
        (400, "CD"),
        (900, "CM"),
        (3999, "MMMCMXCIX"),
        (1, "I"),
    ]

    print("Integer to Roman - Test Results")
    print("-" * 45)

    for index, (num, expected) in enumerate(test_cases, start=1):
        result = solution.intToRoman(num)
        status = "PASS" if result == expected else "FAIL"

        print(f"Test Case {index}: {status}")
        print(f"Input:    {num}")
        print(f"Expected: {expected}")
        print(f"Actual:   {result}")
        print("-" * 45)


if __name__ == "__main__":
    main()
