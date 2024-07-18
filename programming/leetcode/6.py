class Solution:
    def convert(self, s: str, n: int) -> str:
        
        i = 0
        size = len(s)
        converted = []
        while i < size:
            converted.append(s[i:n+i])
            i += n
            for j in range(n-2):
                if i >= size:
                    break
                converted.append(['']*(n-j-2) + [s[i]] +  ['']*(j+1))
                i += 1

        return ''.join(chain.from_iterable(zip_longest(*converted , fillvalue='')))
                
                
        