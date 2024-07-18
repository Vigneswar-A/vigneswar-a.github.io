class Solution:
    def rotateRight(self, head: 'ListNode', k: 'int') -> 'ListNode':
        if not head:return
        if not head.next:return head
        
        dummy=head
        count=1
        while dummy.next:
            dummy=dummy.next
            count+=1
        dummy.next=head
        
        newtail=head
        for _ in range(count-k%count-1):
            newtail=newtail.next
        newhead=newtail.next
        
        newtail.next=None
        
        return newhead
        

            