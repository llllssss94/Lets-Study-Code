from typing import List, Optional
import heapq

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # Heapq is the master key
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        q = []

        # Heap Sort
        for i in range(len(lists)):
            cur = lists[i]
            while cur != None:
                heapq.heappush(q, cur.val)
                cur = cur.next

        # Make Linked List
        head = cur = ListNode()
        for i in range(len(q)):
            cur.next = ListNode(val=heapq.heappop(q))
            cur = cur.next

        return head.next

if __name__ == "__main__":
    lists = [[1,4,5],[1,3,4],[2,6]]
    
    ret = Solution().mergeKLists(lists)
    print(ret)