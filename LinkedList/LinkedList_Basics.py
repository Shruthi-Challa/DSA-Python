class ListNode():
    def __init__(self,val=0):
        self.val = val
        self.next = None
        
    def arraytoLinkedList(arr):
        if not arr:
            return None
            
        head = ListNode(arr[0])
        curr = head
        
        for i in range(1,len(arr)):
            curr.next = ListNode(arr[i])
            curr = curr.next
        return head
        
    def Traversal(head):
        curr = head
        while curr:
            print(curr.val)
            curr=curr.next
            
    def Count(head):
        curr = head
        count = 0
        
        while curr:
            count+=1
            curr = curr.next
            
        return count
        
    def searching(head,target):
        curr = head
        while curr:
            if curr.val == target:
                return "found"
            curr = curr.next
        return "not found"
        
        
arr = [10, 20, 30, 40]
head = ListNode.arraytoLinkedList(arr)

ListNode.Traversal(head)
print(ListNode.Count(head))
print(ListNode.searching(head, 30))
        