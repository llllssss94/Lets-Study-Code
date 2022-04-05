from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # Discussion보면 포인터만 바꿔치는게 더 빠르다고 함
    # 효율적이라고 생각하고 일부러 이렇게 풀었는데 하위 5% ^^!
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # k 만큼 탐색해서 
        # k 만큼 존재하면 reverse 코드 실행
        # k 보다 작은데 None 나오면 그대로 두고 중지

        cur = head

        while cur != None:
            self.revsereK(cur, k)
            for i in range(k):
                if cur == None:
                    break
                cur = cur.next

        return head


    def revsereK(self, head, k):
        # 1 번재 수는 k-1 만큼 거리가 떨어져 있다.
        # 2 번째 수는 k-2 만큼 거리가 떨어져 있다.

        # k 길이면 -> swap을 k // 2 만큼 수행
        swap_cnt = k // 2

        # swap은 현재 node에서 
        
        for i in range(swap_cnt):
            left = head

            # 0이면 실행 안됨 i - 1만큼 앞으로
            for _ in range(i):
                if left == None:
                    break
                left = left.next

            if left == None:
                break

            right = left
            # left에서 첫 바퀴때는 l = k - 1
            # 그다음 부터는 양쪽에서 1씩 줄어드므로 이전 l의 -2
            l = k - 1 - (2 * i)

            # swap할게 없다면 중지
            if l <= 0:
                break
        
            # 바꿔칠 노드 찾기
            for _ in range(l):
                if right == None:
                    break
                right = right.next

            if right == None:
                break

            # 값만 바꿔치셈
            left.val, right.val = right.val, left.val

        

if __name__ == "__main__":
    
    head = [1,2,3,4,5]
    k = 2

    h = cur = ListNode()
    for num in head:
        cur.next = ListNode(val=num)
        cur = cur.next

    ret = Solution().reverseKGroup(h.next, k)
    

    while ret != None:
        print(ret.val)
        ret = ret.next
    
    
    
    head = [1,2,3,4,5]
    k = 3

    h = cur = ListNode()
    for num in head:
        cur.next = ListNode(val=num)
        cur = cur.next

    ret = Solution().reverseKGroup(h.next, k)
    

    while ret != None:
        print(ret.val)
        ret = ret.next