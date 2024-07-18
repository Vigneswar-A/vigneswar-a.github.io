# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        def mergesort(node):
            if node and node.next:
                
                slow,fast = node, node.next
                
                while fast and fast.next:
                    fast = fast.next.next
                    slow = slow.next
                  
                left = node
                right = slow.next
                slow.next = None

                dummy = ListNode()
                curr1 = mergesort(left)
                curr2 = mergesort(right)
                curr = dummy

                while curr1 or curr2:
                    if curr1 and (not curr2 or curr1.val < curr2.val):
                        curr.next = curr1
                        curr1 = curr1.next
                    else:
                        curr.next = curr2
                        curr2 = curr2.next
                    curr = curr.next
                return dummy.next
            
            else:     
                return node
            
        return mergesort(head)
                
            
                    
            
            
        