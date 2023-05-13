class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def merge_sort(head):
    # Base case: if the list is empty or contains only one node
    if not head or not head.next:
        return head

    # Split the list into two halves
    mid = get_middle(head)
    left_half = head
    right_half = mid.next
    mid.next = None

    # Recursively sort the two halves
    left_sorted = merge_sort(left_half)
    right_sorted = merge_sort(right_half)

    # Merge the two sorted halves
    sorted_list = merge(left_sorted, right_sorted)
    return sorted_list


def merge(left, right):
    # Dummy node as the head of the merged list
    dummy = ListNode(0)
    current = dummy

    # Merge the two lists by comparing the values of nodes
    while left and right:
        if left.val < right.val:
            current.next = left
            left = left.next
        else:
            current.next = right
            right = right.next
        current = current.next

    # Attach the remaining nodes from either list
    if left:
        current.next = left
    if right:
        current.next = right

    return dummy.next


def get_middle(head):
    slow = head
    fast = head

    # Move slow pointer one step at a time and fast pointer two steps at a time
    # When fast reaches the end, slow will be at the middle
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next

    return slow


def print_linked_list(head):
    curr = head
    while curr:
        print(curr.val, end=" ")
        curr = curr.next
    print()


# Example usage:
# Create a linked list: 4 -> 2 -> 1 -> 3
head = ListNode(4)
head.next = ListNode(2)
head.next.next = ListNode(1)
head.next.next.next = ListNode(3)

print("Original Linked List:")
print_linked_list(head)

# Sort the linked list using divide and conquer algorithm
sorted_list = merge_sort(head)

print("Sorted Linked List:")
print_linked_list(sorted_list)
