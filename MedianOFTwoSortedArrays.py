
# LeetCode 4: Median of Two Sorted Arrays

class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        # Binary search must be performed on the smaller array.
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m = len(nums1)
        n = len(nums2)

        left = 0
        right = m
        half = (m + n + 1) // 2

        while left <= right:
            i = (left + right) // 2
            j = half - i

            left1 = float("-inf") if i == 0 else nums1[i - 1]
            right1 = float("inf") if i == m else nums1[i]

            left2 = float("-inf") if j == 0 else nums2[j - 1]
            right2 = float("inf") if j == n else nums2[j]

            if left1 <= right2 and left2 <= right1:
                if (m + n) % 2 == 1:
                    return float(max(left1, left2))

                return (
                    max(left1, left2) +
                    min(right1, right2)
                ) / 2.0

            elif left1 > right2:
                right = i - 1

            else:
                left = i + 1

        raise ValueError("Input arrays must be sorted and non-empty in total.")


def main():
    solution = Solution()

    # Example 1: Odd total length
    nums1 = [1, 3]
    nums2 = [2]
    print("Example 1:", solution.findMedianSortedArrays(nums1, nums2))

    # Example 2: Even total length
    nums1 = [1, 2]
    nums2 = [3, 4]
    print("Example 2:", solution.findMedianSortedArrays(nums1, nums2))

    # Additional test: One array is empty
    nums1 = []
    nums2 = [1]
    print("Example 3:", solution.findMedianSortedArrays(nums1, nums2))

    # Additional test: Negative values
    nums1 = [-5, 3, 6]
    nums2 = [-2, 4, 10]
    print("Example 4:", solution.findMedianSortedArrays(nums1, nums2))

    # Additional test: Unequal array sizes
    nums1 = [1, 2, 3, 4, 5]
    nums2 = [6, 7]
    print("Example 5:", solution.findMedianSortedArrays(nums1, nums2))


if __name__ == "__main__":
    main()
