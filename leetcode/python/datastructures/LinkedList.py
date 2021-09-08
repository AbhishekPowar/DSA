# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return f'{self.val}'


class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, val=0, next=None):
        if not self.head:
            self.head = ListNode(val, next)
        else:
            cur = self.head
            while cur.next is not None:
                cur = cur.next
            cur.next = ListNode(val, next)

    def __str__(self):
        values = []
        cur = self.head
        while cur is not None:
            values.append(str(cur))
            cur = cur.next
        values.append('null')
        return ' -> '.join(values)


if __name__ == "__main__":
    ll = LinkedList()
    ll.add(3)
    ll.add(5)
    ll.add(6)
    ll.add(1)
    ll.add(4)
    print(ll)
