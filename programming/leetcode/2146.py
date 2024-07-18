class Solution:
    def placeWordInCrossword(self, board: List[List[str]], word: str) -> bool:   
        boxes = []
        temp1 = []
        temp2 = []
        size = len(word)
        
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] != '#':
                    temp1.append(board[i][j])
                else:
                    if len(temp1) == size:
                        boxes.append(temp1[:])
                    temp1.clear()
            if len(temp1) == size:
                boxes.append(temp1[:]) 
            temp1.clear()
                    
        for i in range(len(board[0])):
            for j in range(len(board)):
                if board[j][i] != '#':
                    temp2.append(board[j][i])
                else:
                    if len(temp2) == size:
                        boxes.append(temp2[:])
                    temp2.clear()           
            if len(temp2) == size:
                boxes.append(temp2[:])
            temp2.clear()
        
        for box in boxes:
            for i in range(len(word)):
                if box[i] == ' ':
                    continue
                elif box[i] != word[i]:
                    break
            else:
                return True
            
            for i in range(len(word)):
                if box[i] == ' ':
                    continue
                elif box[i] != word[-i-1]:
                    break
            else:
                return True
            
        return False
            