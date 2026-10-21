
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        max_area = 0

        while left < right:
            width = right - left
            container_height = min(height[left], height[right])
            area = width * container_height

            max_area = max(max_area, area)

            # Move the pointer at the shorter line.
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area


def main():
    solution = Solution()

    test_cases = [
        ([1, 8, 6, 2, 5, 4, 8, 3, 7], 49),
        ([1, 1], 1),
        ([1, 2, 1], 2),
        ([4, 3, 2, 1, 4], 16),
        ([1, 2, 4, 3], 4),
        ([0, 0], 0),
    ]

    print("Container With Most Water - Test Results")
    print("-" * 45)

    for index, (height, expected) in enumerate(test_cases, start=1):
        result = solution.maxArea(height)
        status = "PASS" if result == expected else "FAIL"

        print(f"Test Case {index}: {status}")
        print(f"Height:   {height}")
        print(f"Expected: {expected}")
        print(f"Actual:   {result}")
        print("-" * 45)


if __name__ == "__main__":
    main()
