
from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)

        closest_sum = nums[0] + nums[1] + nums[2]

        for i in range(n - 2):
            left = i + 1
            right = n - 1

            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]

                if abs(current_sum - target) < abs(closest_sum - target):
                    closest_sum = current_sum

                if current_sum == target:
                    return current_sum

                elif current_sum < target:
                    left += 1

                else:
                    right -= 1

        return closest_sum


def main():
    solution = Solution()

    test_cases = [
        ([-1, 2, 1, -4], 1, 2),
        ([0, 0, 0], 1, 0),
        ([1, 1, 1, 0], -100, 2),
        ([1, 1, -1, -1, 3], 1, 1),
        ([4, 0, 5, -5, 3, 3, 0, -4], 1, 2),
        ([1, 2, 4, 8, 16, 32, 64, 128], 82, 82),
    ]

    print("3Sum Closest - Test Results")
    print("-" * 50)

    for index, (nums, target, expected) in enumerate(test_cases, start=1):
        result = solution.threeSumClosest(nums.copy(), target)
        status = "PASS" if result == expected else "FAIL"

        print(f"Test Case {index}: {status}")
        print(f"Input:    {nums}")
        print(f"Target:   {target}")
        print(f"Expected: {expected}")
        print(f"Actual:   {result}")
        print("-" * 50)


if __name__ == "__main__":
    main()
