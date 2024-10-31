class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return 'Zero'
        powers = ['', 'Thousand', 'Million', 'Billion']
        ones = ['', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
        tens = ['Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen']
        hundreds = ['', 'Ten', 'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']
        
        
        def convert(num):
            if int(num) == 0:
                return ''
            num = str(int(num))
            if len(num) == 1:
                return ones[int(num)]
            if len(num) == 2:
                if int(num) == 10:
                    return 'Ten'
                elif int(num) < 20:
                    return tens[int(num)-10]
                else:
                    return hundreds[int(num)//10]+' '+(ones[int(num)%10] if int(num)%10 else '')
            if len(num) == 3:
                return convert(num[0])+' Hundred '+convert(num[1:])
        res = ''
        for i, num in enumerate(reversed(f'{num:,}'.split(','))):
            res = convert(num) + ' ' + (powers[i] if int(num) else '') + ' ' + res
            
        return ' '.join(res.split())
        
                
        
        
        
        
        
        