
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        Trie = lambda : defaultdict(Trie)       
        root = Trie()
        
        for product in products:
            reduce(dict.__getitem__ , product , root)['*'] = '*'
            
        def get_words(node):           
            heap = [('',node)]
            heapq.heapify(heap)
            words = []
            count = 0
            while heap and count < 3:
                word , node = heapq.heappop(heap)
                
                for c in node:
                    if c != '*':
                        heapq.heappush(heap , (word + c , node[c]))
                    else:
                        words.append(temp + word)
                        count += 1

            return words
        
        res = []
        curr = root
        temp = ''
        for c in searchWord:
            temp += c
            curr = curr[c]
            res.append(get_words(curr))
            
            
        return res      