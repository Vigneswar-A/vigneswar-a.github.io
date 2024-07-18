class Solution:
    def reorderSpaces(self, text: str) -> str:
        

        space_count = text.count(" ")
        words = text.split()
        
        if len(words) == 1:
            return words[0] + " "*space_count
        
        for_each,extra = divmod(space_count, len(words)-1)
        
        return (" "*for_each).join(words) + " "*extra