from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:        
        cur = head
        length = 0
        while cur != None:
            cur = cur.next
            length += 1

        if length == 1:
            return head
        
        # left 수 찾기
        l = head
        cnt = 1
        while True:
            if cnt == k:
                break
            cnt += 1
            l = l.next

        # right 수 찾기
        cnt = 0
        r = head
        while True:
            cnt += 1
            if cnt == length - k + 1:
                break
            r = r.next
        
        # 값만 바꿔쳐
        tmp = r.val
        r.val = l.val
        l.val = tmp

        return head
        

        

if __name__ == "__main__":
    
    head = [1,2,3,4,5]
    k = 4

    i = h = ListNode()

    for n in head:
        h.next = ListNode(val=n)
        h = h.next

    ret = Solution().swapNodes(i.next, k)
    
    while ret != None:
        print(ret.val)
        ret = ret.next


    head = [7,9,6,6,7,8,3,0,9,5]
    k = 5

    i = h = ListNode()

    for n in head:
        h.next = ListNode(val=n)
        h = h.next

    ret = Solution().swapNodes(i.next, k)
    
    while ret != None:
        print(ret.val)
        ret = ret.next

    
    

    head = [80,46,66,35,64]
    k = 1

    i = h = ListNode()

    for n in head:
        h.next = ListNode(val=n)
        h = h.next

    ret = Solution().swapNodes(i.next, k)
    
    while ret != None:
        print(ret.val)
        ret = ret.next