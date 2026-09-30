# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # input: 2, 4, 6, 8
        # output: 2, 8, 4, 6

        # input: 2, 4, 6, 8, 10
        # output: 2, 10, 4, 8, 6
        # pattern: front, back, front, back, front

        # brute force: copy all the nodes into an array
        # then use two pointers with one in the front and one in the back
        # relink the nodes in the new order
        # time: O(n)
        # space: O(n)

        # split the list in the middle, giving us the front and back of the list
        # reverse the back of the list
        # merge the two lists

        # time: O(n)
        # space: O(1)

        # find middle of linked lists
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        second = slow.next
        slow.next = None

        # reverse second half of linked list
        prev = None
        curr = second

        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        second = prev

        # merge first and second half of linked list
        first = head
        while second:
            first_next = first.next
            second_next = second.next

            first.next = second
            second.next = first_next

            first = first_next
            second = second_next

