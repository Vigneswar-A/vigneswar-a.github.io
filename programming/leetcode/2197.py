class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        cols = ceil(len(encodedText)/rows)
        res = ''
        for i in range(cols):
            for j in range(rows):
                res += encodedText[cols*j+i+j] if cols*j+i+j < len(encodedText) else ''
  
                
                
        return res.rstrip()
        
        
        