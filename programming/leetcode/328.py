# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        odd,even=ListNode(),ListNode()
        pointerodd,pointereven,pointer,i=odd,even,head,0

        while pointer:
            i+=1
            if i%2:
                pointerodd.next=pointer
                pointerodd=pointerodd.next
            else:
                pointereven.next=pointer
                pointereven=pointereven.next
            pointer=pointer.next
            
        if i:
            pointereven.next=None
            
        pointerodd.next=even.next
        return odd.next
                
            
        