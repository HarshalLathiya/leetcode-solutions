# LeetCode 1: Add Two Numbers
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1, l2):
        dummy = ListNode()
        current = dummy
        carry = 0

        while l1 or l2 or carry:
            digit1 = l1.val if l1 else 0
            digit2 = l2.val if l2 else 0

            total = digit1 + digit2 + carry
            digit = total % 10
            carry = total // 10

            current.next = ListNode(digit)
            current = current.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return dummy.next


# Helper function to create a linked list
def create_list(values):
    dummy = ListNode()
    current = dummy

    for value in values:
        current.next = ListNode(value)
        current = current.next

    return dummy.next


# Helper function to print a linked list
def print_list(node):
    values = []

    while node:
        values.append(str(node.val))
        node = node.next

    print(" -> ".join(values))


# Test the solution: 342 + 465 = 807
l1 = create_list([2, 4, 3])
l2 = create_list([5, 6, 4])

solution = Solution()
result = solution.addTwoNumbers(l1, l2)

print("Result:")
print_list(result)
