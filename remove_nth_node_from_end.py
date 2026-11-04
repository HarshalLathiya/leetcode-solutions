
from typing import Optional, List


# Define a Linked List Node
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(
        self,
        head: Optional[ListNode],
        n: int
    ) -> Optional[ListNode]:

        # Create dummy node.
        dummy = ListNode(0, head)

        fast = dummy
        slow = dummy

        # Move fast n + 1 steps ahead.
        for _ in range(n + 1):
            fast = fast.next

        # Move both pointers until fast reaches None.
        while fast:
            fast = fast.next
            slow = slow.next

        # Remove the target node.
        slow.next = slow.next.next

        return dummy.next


# Convert Python list into Linked List.
def create_linked_list(values: List[int]) -> Optional[ListNode]:
    dummy = ListNode()
    current = dummy

    for value in values:
        current.next = ListNode(value)
        current = current.next

    return dummy.next


# Convert Linked List into Python list.
def linked_list_to_list(head: Optional[ListNode]) -> List[int]:
    result = []

    current = head

    while current:
        result.append(current.val)
        current = current.next

    return result


def main():
    solution = Solution()

    test_cases = [
        ([1, 2, 3, 4, 5], 2, [1, 2, 3, 5]),
        ([1], 1, []),
        ([1, 2], 1, [1]),
        ([1, 2], 2, [2]),
        ([1, 2, 3, 4, 5], 5, [2, 3, 4, 5]),
        ([1, 2, 3], 3, [2, 3]),
    ]

    print("Remove Nth Node From End - Test Results")
    print("-" * 55)

    for index, (values, n, expected) in enumerate(test_cases, start=1):

        head = create_linked_list(values)

        result_head = solution.removeNthFromEnd(head, n)

        actual = linked_list_to_list(result_head)

        status = "PASS" if actual == expected else "FAIL"

        print(f"Test Case {index}: {status}")
        print(f"Input:    {values}")
        print(f"n:        {n}")
        print(f"Expected: {expected}")
        print(f"Actual:   {actual}")
        print("-" * 55)


if __name__ == "__main__":
    main()
