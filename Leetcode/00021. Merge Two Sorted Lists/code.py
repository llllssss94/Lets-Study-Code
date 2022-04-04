from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()

        cur = head
        while list1 != None and list2 != None:
            if list1.val >= list2.val:
                cur.next = ListNode(list2.val)
                list2 = list2.next
                cur = cur.next
            elif list1.val < list2.val:
                cur.next = ListNode(list1.val)
                list1 = list1.next
                cur = cur.next

        if list1 != None:
            while list1 != None:
                cur.next = ListNode(list1.val)
                list1 = list1.next
                cur = cur.next

        elif list2 != None:
            while list2 != None:
                cur.next = ListNode(list2.val)
                list2 = list2.next
                cur = cur.next
        
        return head.next
        

if __name__ == "__main__":
    list1 = ListNode()
    list2 = ListNode()

    cur = list1
    for num in []:
        cur.next = ListNode(val=num)
        cur = cur.next
        
    cur = list2
    for num in []:
        cur.next = ListNode(val=num)
        cur = cur.next

    ret = Solution().mergeTwoLists(list1.next, list2.next)
    
    while ret != None:
        print(ret.val)
        ret = ret.next

    
    list1 = ListNode()
    list2 = ListNode()

    cur = list1
    for num in []:
        cur.next = ListNode(val=num)
        cur = cur.next
        
    cur = list2
    for num in [0]:
        cur.next = ListNode(val=num)
        cur = cur.next

    ret = Solution().mergeTwoLists(list1.next, list2.next)

    
    while ret != None:
        print(ret.val)
        ret = ret.next


        
    list1 = ListNode()
    list2 = ListNode()

    cur = list1
    for num in [1, 2, 4]:
        cur.next = ListNode(val=num)
        cur = cur.next
        
    cur = list2
    for num in [1, 3, 4]:
        cur.next = ListNode(val=num)
        cur = cur.next

    ret = Solution().mergeTwoLists(list1.next, list2.next)

    
    while ret != None:
        print(ret.val)
        ret = ret.next