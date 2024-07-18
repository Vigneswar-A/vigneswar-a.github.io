class Solution:
    def findComplement(self, num: int) -> int:
        s=''
        for i in str(bin(num))[2:]:
            if i=='1':
                s+='0'
            else:
                s+='1'
        return int(s,2)
        