
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        first = strs[0]

        for i in range(len(first)):
            current_char = first[i]

            for string in strs[1:]:
                if i >= len(string) or string[i] != current_char:
                    return first[:i]

        return first


def main():
    solution = Solution()

    test_cases = [
        (["flower", "flow", "flight"], "fl"),
        (["dog", "racecar", "car"], ""),
        (["interspecies", "interstellar", "interstate"], "inters"),
        (["apple", "apple", "apple"], "apple"),
        (["a"], "a"),
        (["", "abc"], ""),
        (["ab", "a"], "a"),
        (["abc", "abcd", "abce"], "abc"),
    ]

    print("Longest Common Prefix - Test Results")
    print("-" * 45)

    for index, (strs, expected) in enumerate(test_cases, start=1):
        result = solution.longestCommonPrefix(strs)
        status = "PASS" if result == expected else "FAIL"

        print(f"Test Case {index}: {status}")
        print(f"Input:    {strs}")
        print(f"Expected: {expected!r}")
        print(f"Actual:   {result!r}")
        print("-" * 45)


if __name__ == "__main__":
    main()
