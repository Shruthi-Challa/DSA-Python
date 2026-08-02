class Solution(object):
    def reverseKGroup(self, head, k):
        dummy = ListNode(0)
        dummy.next = head
        curr = head
        prev_group = dummy
        

        while True:
            kth=prev_group
            for _ in range(k):
                kth=kth.next
                if not kth:
                    return dummy.next
                    
            group_next=kth.next
            prev=group_next
            curr = prev_group.next
            
            while curr!=group_next:
                nxt = curr.next
                curr.next=prev
                prev=curr
                curr = nxt

            group_start = prev_group.next
            prev_group.next = kth
            prev_group = group_start

        return dummy.next