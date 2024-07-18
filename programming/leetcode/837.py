class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        # going to populate set with O(1) lookup time in comparison to O(n)
        banned = set(banned)
            
        # purge all symbols
        for i in "!?',;.":
            paragraph = paragraph.replace(i, " ")
        
        words = {}
        
        paragraph = paragraph.lower()        
        
        # two choices here:
        #   .split()      O(n) space
        #   two pointers  O(1)
        # both will require O(n) time, so we should go ahead and pick the optimal space solution
        
        p1, p2 = 0, 0
        
        while p2 <= len(paragraph):
            if p2 == len(paragraph) or paragraph[p2] == " ":  # if we are at the end of a word / paragraph
                word = paragraph[p1:p2]     # pick up the word
                if word not in banned:
                    if word in words:
                        words[word] += 1
                    else:
                        words[word] = 1
                # find next word, or end, whichever comes first
                while p2 < len(paragraph) and paragraph[p2] == " ":
                    p2 += 1
                
                p1 = p2
            p2 += 1
            
        return  max(words, key=words.get)