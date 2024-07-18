# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        array = []
        
        while head:
            array.append(head.val)
            head = head.next
            
        while True:
            hashmap = {0:-1}
            currsum = 0
            for i in range(len(array)):
                currsum += array[i]
                if currsum in hashmap:
                    array[hashmap[currsum]+1:i+1] = []
                    break
                hashmap[currsum] = i
            else:
                break
                
        sentinel = ListNode()
        currnode = sentinel
        for num in array:
            currnode.next = ListNode(num)
            currnode = currnode.next
            
        return sentinel.next
                
        