class Solution(object):
    def partition(self, head, x):
        lessdummy = ListNode(0)
        greaterdummy = ListNode(0)

        less=lessdummy
        greater = greaterdummy

        curr = head
        while curr:
            if curr.val < x:
                less.next=curr
                less=less.next

            else:
                greater.next=curr
                greater = greater.next

            curr = curr.next 

        greater.next=None
        less.next = greaterdummy.next

        return lessdummy.next  