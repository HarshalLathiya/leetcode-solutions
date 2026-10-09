
# LeetCode 3: Longest Substring Without Repeating Characters
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_seen = {}
        left = 0
        max_length = 0

        for right, char in enumerate(s):
            # If the character repeats inside the current window,
            # move the left pointer beyond its previous occurrence.
            if char in last_seen:
                left = max(left, last_seen[char] + 1)

            # Store the latest index of the character.
            last_seen[char] = right

            # Calculate the current window length.
            current_length = right - left + 1

            # Keep the maximum length found so far.
            max_length = max(max_length, current_length)

        return max_length


def main():
    solution = Solution()

    # Example 1
    s = "abcabcbb"
    print(f'Input: "{s}"')
    print("Output:", solution.lengthOfLongestSubstring(s))
    print()

    # Example 2
    s = "bbbbb"
    print(f'Input: "{s}"')
    print("Output:", solution.lengthOfLongestSubstring(s))
    print()

    # Example 3
    s = "pwwkew"
    print(f'Input: "{s}"')
    print("Output:", solution.lengthOfLongestSubstring(s))
    print()

    # Additional test cases
    test_cases = [
        "",
        "au",
        "dvdf",
        "abba",
        "a b a",
    ]

    print("Additional test cases:")
    for s in test_cases:
        result = solution.lengthOfLongestSubstring(s)
        print(f"{s!r} -> {result}")


if __name__ == "__main__":
    main()
