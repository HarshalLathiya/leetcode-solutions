# LeetCode #21 - Merge Two Sorted Lists


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1, list2):

        # Dummy node simplifies list construction
        dummy = ListNode(0)
        current = dummy

        # Compare nodes from both lists
        while list1 and list2:

            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next

            current = current.next

        # Attach remaining nodes
        if list1:
            current.next = list1
        else:
            current.next = list2

        # Skip dummy node
        return dummy.next


# Convert Python list to Linked List
def create_linked_list(values):

    dummy = ListNode(0)
    current = dummy

    for value in values:
        current.next = ListNode(value)
        current = current.next

    return dummy.next


# Convert Linked List to Python list
def linked_list_to_list(head):

    result = []

    while head:
        result.append(head.val)
        head = head.next

    return result


def main():

    solution = Solution()

    # Test Case 1
    list1 = create_linked_list([1, 2, 4])
    list2 = create_linked_list([1, 3, 4])

    result = solution.mergeTwoLists(list1, list2)

    print("Test Case 1")
    print("List 1 : [1, 2, 4]")
    print("List 2 : [1, 3, 4]")
    print("Output :", linked_list_to_list(result))
    print()

    # Test Case 2
    list1 = create_linked_list([])
    list2 = create_linked_list([])

    result = solution.mergeTwoLists(list1, list2)

    print("Test Case 2")
    print("List 1 : []")
    print("List 2 : []")
    print("Output :", linked_list_to_list(result))
    print()

    # Test Case 3
    list1 = create_linked_list([])
    list2 = create_linked_list([0])

    result = solution.mergeTwoLists(list1, list2)

    print("Test Case 3")
    print("List 1 : []")
    print("List 2 : [0]")
    print("Output :", linked_list_to_list(result))
    print()

    # Test Case 4
    list1 = create_linked_list([1, 2, 2])
    list2 = create_linked_list([1, 2, 3])

    result = solution.mergeTwoLists(list1, list2)

    print("Test Case 4")
    print("List 1 : [1, 2, 2]")
    print("List 2 : [1, 2, 3]")
    print("Output :", linked_list_to_list(result))


if __name__ == "__main__":
    main()