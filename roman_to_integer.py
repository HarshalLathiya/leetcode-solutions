
class Solution:
    def romanToInt(self, s: str) -> int:
        values = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        total = 0

        for i in range(len(s)):
            current = values[s[i]]

            if i + 1 < len(s) and current < values[s[i + 1]]:
                total -= current
            else:
                total += current

        return total


def main():
    solution = Solution()

    test_cases = [
        ("III", 3),
        ("LVIII", 58),
        ("MCMXCIV", 1994),
        ("IV", 4),
        ("IX", 9),
        ("XL", 40),
        ("XC", 90),
        ("CD", 400),
        ("CM", 900),
        ("MMMCMXCIX", 3999),
        ("I", 1),
    ]

    print("Roman to Integer - Test Results")
    print("-" * 45)

    for index, (roman, expected) in enumerate(test_cases, start=1):
        result = solution.romanToInt(roman)
        status = "PASS" if result == expected else "FAIL"

        print(f"Test Case {index}: {status}")
        print(f"Input:    {roman}")
        print(f"Expected: {expected}")
        print(f"Actual:   {result}")
        print("-" * 45)


if __name__ == "__main__":
    main()
