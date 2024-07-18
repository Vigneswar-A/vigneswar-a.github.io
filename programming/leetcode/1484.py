# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        
        @cache
        def search(listnode, treenode):
            if listnode is None:
                return True

            if not treenode:
                return False

            if listnode.val == treenode.val and (search(listnode.next, treenode.left) or search(listnode.next, treenode.right)):
                return True
            
            return search(head, treenode.left) or search(head, treenode.right)
        
        return search(head, root)
        