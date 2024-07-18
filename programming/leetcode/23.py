# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        def break_list(list):
            res = []
            while list:
                res.append(list.val)
                list = list.next
            return res

        def generate_list(list):
            dummy = ListNode()
            currnode = dummy
            for i in list:
                currnode.next = ListNode(i)
                currnode = currnode.next
            return dummy.next

        return generate_list(sorted(sum(map(break_list, lists), [])))