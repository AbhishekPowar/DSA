from datastructures.LinkedList import *
from typing import *


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head:
            prev, cur, nextt = None, head, head.next
            while True:
                cur.next = prev
                if nextt is None:
                    break
                prev, cur, nextt = cur, nextt, nextt.next
            head = cur
        return head

    def reverseListRecursive(self, head):
        if head and head.next:
            cur = head
            nextt = cur.next
            cur.next = None
            newHead = Solution().reverseListRecursive(nextt)
            nextt.next = cur
            return newHead
        return head


if __name__ == "__main__":
    ll = LinkedList()
    # newHead = Solution().reverseList(ll.head)
    ll.add(3)
    ll.add(2)
    ll.add(5)
    ll.add(8)
    newHead = Solution().reverseListRecursive(ll.head)
    ll.head = newHead
    print(ll)
