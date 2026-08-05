class Solution(object):
    def rotateRight(self, head, k):
        if not head or k==0 or not head.next:
            return head

        length = 1
        tail = head
        while tail.next:
            tail = tail.next
            length+=1

        rotations = k % length
        if rotations == 0:
            return head

        tail.next = head
        position = length - rotations -1

        new_tail = head
        for _ in range(1,position+1):
            new_tail = new_tail.next

        new_head = new_tail.next
        new_tail.next = None

        return new_head