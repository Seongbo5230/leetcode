# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:

        retNode = ListNode(-1)
        tempNode = retNode

        while l1 and l2:
            if l1.val <= l2.val:
                tempNode.next = l1
                l1 = l1.next
            else:
                tempNode.next = l2
                l2 = l2.next
            tempNode = tempNode.next

        tempNode.next = l1 if l1 is not None else l2

        return retNode.next

def main():
    l1 = ListNode(1)
    l2 = ListNode(2)
    l3 = ListNode(4)
    l1.next = l2
    l2.next = l3

    r1 = ListNode(1)
    r2 = ListNode(3)
    r3 = ListNode(4)
    r1.next = r2
    r2.next = r3

    soln = Solution()
    soln.mergeTwoLists(l1, r1)

if __name__ == "__main__":
    main()
