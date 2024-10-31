# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        
        directions = [(0,1),(1,0),(0,-1),(-1,0)]
        limit = [0, 0, m, n]
        
        x = 0
        y = 0
        res = [[-1]*n for _ in range(m)]
        d = 0
        while head and head.val != -1:
            
            res[x][y] = head.val
            dx, dy = directions[d]
            
            
            if x+dx == m or y+dy == n or x+dx == -1 or y+dy == -1 or res[x+dx][y+dy] != -1:
                d = (d+1)%4
                dx, dy = directions[d]
            x += dx
            y += dy
            
            head = head.next
            
        return res
        
        
       
        