class Solution(object):
    def mergeTwoLists(self, list1, list2):
        dummy = ListNode(0)
        tail = dummy

        while list1 and list2:
            val1=list1 if list1 else 0 
            val2=list2 if list2 else 0

            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
                tail=tail.next 

            else:
                tail.next = list2
                list2 = list2.next
                tail = tail.next

        if list1:
            tail.next = list1
        else:
            tail.next = list2

        return dummy.next
