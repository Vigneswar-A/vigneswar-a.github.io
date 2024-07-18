class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:
        convert = lambda word : ([(sum(1 for _ in i) , c) for c , i in groupby(word)] , word)
        letters , _ = convert(s)
        size = len(letters)

        word_letters = [*map(convert , words)]
        res = 0
        
        for word , string in word_letters:
            flag = True
            
            if len(word) != size:
                continue
                
            for i in range(size):
                if word[i][1] != letters[i][1] or word[i][0] > letters[i][0] \
                if word[i][0] > 2 else letters[i][0] < 3 and word[i][0] != letters[i][0]:
                    flag = False
                    break
            
            if flag: 
                res += 1
        
        del word_letters
        return res
                
                
                        
                
                
                
        
        
        