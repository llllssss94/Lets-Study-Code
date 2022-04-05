from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head

        if cur is None:
            return
        
        cnt = 0
        while cur.next != None:
            if cnt % 2 == 0:
                self.swap(cur)
            # 2번 앞으로
            cur = cur.next
            cnt += 1
        
        return head


    def swap(self, left):
        left.next.val, left.val = left.val, left.next.val
    

if __name__ == "__main__":
    head = [1, 2, 3, 4]

    h = cur = ListNode()
    for num in head:
        cur.next = ListNode(val=num)
        cur = cur.next

    ret = Solution().swapPairs(h.next)
    
    while ret != None:
        print(ret.val)
        ret = ret.next

    
    
    head = []

    h = cur = ListNode()
    for num in head:
        cur.next = ListNode(val=num)
        cur = cur.next

    ret = Solution().swapPairs(h.next)
    
    while ret != None:
        print(ret.val)
        ret = ret.next

    
    
    head = [1]

    h = cur = ListNode()
    for num in head:
        cur.next = ListNode(val=num)
        cur = cur.next

    ret = Solution().swapPairs(h.next)
    
    while ret != None:
        print(ret.val)
        ret = ret.next