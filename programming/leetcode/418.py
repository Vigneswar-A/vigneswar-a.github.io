class Solution:
    def wordsTyping(self, sentence: List[str], rows: int, cols: int) -> int:

        lengths = [len(word) for word in sentence]
        n = len(lengths)
        
        @cache
        def fill_row(idx):
            col = 0
            while col + lengths[idx%n] <= cols:
                if col + lengths[idx%n] < cols:
                    col += lengths[idx%n] + 1
                    idx += 1
                elif col + lengths[idx%n] == cols:
                    return idx+1
            return idx
            
        ans = 0
        idx = 0
        for _ in range(rows):
            idx = fill_row(idx)
            ans += idx//n
            idx = idx%n
            
        return ans
                
            
                
                    
                    


