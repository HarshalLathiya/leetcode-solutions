
# LeetCode 1: Two Sum
class Solution:
    def twoSum(self, nums, target):
        seen = {}

        for i, num in enumerate(nums):
            complement = target - num

            if complement in seen:
                return [seen[complement], i]

            seen[num] = i

        return []


def main():
    solution = Solution()

    # Example 1
    nums = [2, 7, 11, 15]
    target = 9
    print("Example 1:", solution.twoSum(nums, target))

    # Example 2
    nums = [3, 2, 4]
    target = 6
    print("Example 2:", solution.twoSum(nums, target))

    # Example 3: Duplicate numbers
    nums = [3, 3]
    target = 6
    print("Example 3:", solution.twoSum(nums, target))

    # Additional test: Negative numbers
    nums = [-3, 4, 3, 90]
    target = 0
    print("Extra test:", solution.twoSum(nums, target))


if __name__ == "__main__":
    main()
