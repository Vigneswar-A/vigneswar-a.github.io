class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        def get_head(num):
            s = f"{int(bin(num)[2:]):0>8}"
            i = 0
            while i < len(s) and s[i] == '1':
                i += 1
            return i
        
        flag = 0
        for i in map(get_head, data):
            if (not flag and i == 1) or i > 4:
                return False
            if flag == 0:
                flag = max(0, i-1)
                continue
            elif i != 1:
                return False
            flag -= 1
            
        return flag == 0
        