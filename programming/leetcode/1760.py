class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        pos = {a: i for i, a in enumerate(arr) }
        seen = 0
        
        for piece in pieces:
            if piece[0] in pos:
                pos_i = pos[piece[0]]
                match = True
                for p in piece:
                    if pos_i >= len(arr):
                        return False
                    if p != arr[pos_i]:
                        return False
                    pos_i += 1
                if match:
                    seen += len(piece)
        return seen == len(arr)