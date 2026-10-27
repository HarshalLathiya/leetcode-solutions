
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        n = len(nums)

        for i in range(n - 2):
            # Skip duplicate first values.
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # No valid triplet can start with a positive number.
            if nums[i] > 0:
                break

            left = i + 1
            right = n - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total == 0:
                    result.append([nums[i], nums[left], nums[right]])

                    left += 1
                    right -= 1

                    # Skip duplicate second values.
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

                    # Skip duplicate third values.
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

                elif total < 0:
                    left += 1
                else:
                    right -= 1

        return result


def main():
    solution = Solution()

    test_cases = [
        ([-1, 0, 1, 2, -1, -4],
         [[-1, -1, 2], [-1, 0, 1]]),

        ([0, 1, 1], []),

        ([0, 0, 0],
         [[0, 0, 0]]),

        ([-2, 0, 1, 1, 2],
         [[-2, 0, 2], [-2, 1, 1]]),

        ([-1, -1, -1, 0, 1, 1],
         [[-1, 0, 1]]),

        ([1, 2, -2, -1],
         []),

        ([-4, -2, -2, -2, 0, 2, 2, 2, 4],
         [[-4, 0, 4], [-2, -2, 4], [-2, 0, 2]]),
    ]

    print("3Sum - Test Results")
    print("-" * 50)

    for index, (nums, expected) in enumerate(test_cases, start=1):
        actual = solution.threeSum(nums.copy())

        # Compare results independent of triplet ordering.
        passed = sorted(map(tuple, actual)) == sorted(map(tuple, expected))
        status = "PASS" if passed else "FAIL"

        print(f"Test Case {index}: {status}")
        print(f"Input:    {nums}")
        print(f"Expected: {expected}")
        print(f"Actual:   {actual}")
        print("-" * 50)


if __name__ == "__main__":
    main()
