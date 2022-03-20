
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1, l2):
        carry = 0
        answer = ListNode()

        # 뒤에서 부터 읽어야 하므로 저장해 놓기
        start_node = answer

        # l1, l2에서 모두 꺼낼때 까지
        while l1 or l2:
            v1 = 0
            v2 = 0

            if l1:
                v1, l1 = l1.val, l1.next

            if l2:
                v2, l2 = l2.val, l2.next
            
            # 더한 값의 1의 자리수 노드 추가
            answer.next = ListNode(val = (v1 + v2 + carry) % 10)
            # 1의자리수 제외한 값을 carry값으로
            carry = (v1 + v2 + carry) // 10
            # 다음자리수로 넘어감
            answer = answer.next

        # 마지막에 더한 값이 10보다 크면 1개 남음
        if carry:
            answer.next = ListNode(carry)

        # 첫번째는 시작점이므로 2번째부터 숫자
        return start_node.next

if __name__ == "__main__":
    l1 = None
    for i in [2,4,3]:
        l1 = ListNode(val=i, next=l1)

    l2 = None
    for i in [5,6,4]:
        l2 = ListNode(val=i, next=l2)

    ret = Solution().addTwoNumbers(l1, l2)
    while ret != None:
        print(ret.val)
        ret = ret.next

    print('----------------')


    l1 = None
    for i in [2,4,9]:
        l1 = ListNode(val=i, next=l1)

    l2 = None
    for i in [5,6,4,9]:
        l2 = ListNode(val=i, next=l2)

    ret = Solution().addTwoNumbers(l1, l2)
    while ret != None:
        print(ret.val)
        ret = ret.next


    print('----------------')
    l1 = None
    for i in [0]:
        l1 = ListNode(val=i, next=l1)

    l2 = None
    for i in [0]:
        l2 = ListNode(val=i, next=l2)


    ret = Solution().addTwoNumbers(l1, l2)    
    while ret != None:
        print(ret.val)
        ret = ret.next

    print('----------------')
    l1 = None
    for i in [5, 6]:
        l1 = ListNode(val=i, next=l1)
        
    l2 = None
    for i in [5, 4, 9]:
        l2 = ListNode(val=i, next=l2)

    ret = Solution().addTwoNumbers(l1, l2)    
    while ret != None:
        print(ret.val)
        ret = ret.next

