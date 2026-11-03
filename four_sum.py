
from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()

        result = []
        n = len(nums)

        for i in range(n - 3):

            # Skip duplicate first elements.
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            for j in range(i + 1, n - 2):

                # Skip duplicate second elements.
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue

                left = j + 1
                right = n - 1

                while left < right:

                    total = (
                        nums[i] + nums[j] +
                        nums[left] + nums[right]
                    )

                    if total == target:
                        result.append([
                            nums[i], nums[j],
                            nums[left], nums[right]
                        ])

                        left += 1
                        right -= 1

                        # Skip duplicate left values.
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1

                        # Skip duplicate right values.
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1

                    elif total < target:
                        left += 1

                    else:
                        right -= 1

        return result


def main():
    solution = Solution()

    test_cases = [
        (
            [1, 0, -1, 0, -2, 2],
            0,
            [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]
        ),
        (
            [2, 2, 2, 2, 2],
            8,
            [[2, 2, 2, 2]]
        ),
        (
            [0, 0, 0, 0],
            0,
            [[0, 0, 0, 0]]
        ),
        (
            [-3, -1, 0, 2, 4, 5],
            2,
            [[-3, -1, 2, 4]]
        ),
        (
            [1, 2, 3, 4],
            100,
            []
        ),
        (
            [-2, -2, -2, -2, 2, 2, 2, 2],
            0,
            [[-2, -2, 2, 2]]
        ),
        (
            [0, 0, 0, 0, 0],
            1,
            []
        )
    ]

    print("4Sum - Test Results")
    print("-" * 55)

    for index, (nums, target, expected) in enumerate(test_cases, start=1):

        actual = solution.fourSum(nums.copy(), target)

        # Compare results independent of output ordering.
        passed = sorted(map(tuple, actual)) == sorted(map(tuple, expected))

        status = "PASS" if passed else "FAIL"

        print(f"Test Case {index}: {status}")
        print(f"Input:    {nums}")
        print(f"Target:   {target}")
        print(f"Expected: {expected}")
        print(f"Actual:   {actual}")
        print("-" * 55)


if __name__ == "__main__":
    main()
