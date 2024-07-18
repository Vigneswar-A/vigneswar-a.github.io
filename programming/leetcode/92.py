# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        my_list = []
        while head:
            my_list.append(head)
            head = head.next
            
        
        my_list[left-1:right] = my_list[left-1:right][::-1]
        
        for i in range(len(my_list)-1):
            my_list[i].next = my_list[i+1]
            
        my_list[-1].next = None
        return my_list[0]