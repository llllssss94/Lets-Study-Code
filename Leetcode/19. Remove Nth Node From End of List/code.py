from posixpath import curdir
from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        h = ListNode(val=None, next=head)
        cur = h

        l = 0
        # Find length of linked list
        while cur != None:
            cur = cur.next
            l += 1
        

        i = 0
        cur = h
        while True:
            if i == l - n - 1:
                cur.next = cur.next.next
                break

            cur = cur.next
            i += 1
        
        return h.next

if __name__ == "__main__":
    head = [1,2,3,4,5]
    n = 2

    h = cur = ListNode(val = head[0], next = None)
    for i in range(1, len(head)):
        cur.next = ListNode(val = head[i], next = None)
        cur = cur.next

    ret = Solution().removeNthFromEnd(h, n)

    while ret != None:
        print(ret.val)
        ret = ret.next


        
    head = [1]
    n = 1

    h = cur = ListNode(val = head[0], next = None)
    for i in range(1, len(head)):
        cur.next = ListNode(val = head[i], next = None)
        cur = cur.next

    ret = Solution().removeNthFromEnd(h, n)

    while ret != None:
        print(ret.val)
        ret = ret.next


        
    head = [1,2]
    n = 2

    h = cur = ListNode(val = head[0], next = None)
    for i in range(1, len(head)):
        cur.next = ListNode(val = head[i], next = None)
        cur = cur.next

    ret = Solution().removeNthFromEnd(h, n)

    while ret != None:
        print(ret.val)
        ret = ret.next