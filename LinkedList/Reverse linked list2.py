class Solution(object):
    def reverseBetween(self, head, left, right):
        if not head or left == right:
            return head

        prev = None
        curr = head
        pos = 1

        while pos < left:
            prev = curr
            curr = curr.next
            pos += 1

        con = prev
        tail=curr

        rev_prev = None
        count = right - left + 1

        while count > 0:
            nxt = curr.next
            curr.next = rev_prev
            rev_prev = curr
            curr = nxt

            count -=1

        if con:
            con.next = rev_prev
        else:
            head = rev_prev

        tail.next = curr

        return head