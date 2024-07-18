class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        
        @cache
        def dp(idx=0, width=0, curr_height=0):
            if width > shelfWidth:
                return inf
            
            if idx == len(books):
                return curr_height
            
            book_width, book_height = books[idx]
            
            return min(
                dp(idx+1, width+book_width, max(curr_height, book_height)),
                dp(idx+1, book_width, book_height)+curr_height
            )
        
        return dp()
        
        