class Solution:
    def discountPrices(self, sentence: str, discount: int) -> str:
        discount /= 100
        res = ''
        pattern = re.compile(r'\$[0-9.]+')
        for word in sentence.split():
            if pattern.fullmatch(word):
                res += '$' + f'%.2f '%(int(word[1:]) - int(word[1:]) * discount)
            else:
                res += word + ' '
                
        return res[:-1]
            
        