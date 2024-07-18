digits={1000:'M',900:'CM',500:'D',400:'CD',100:'C',90:'XC',50:'L',40:'XL',10:'X',9:'IX',5:'V',4:'IV',1:'I'}
class Solution:
    def intToRoman(self, num: int) -> str:    
        roman=''
        while num>0:
            for i in digits.keys():
                if num>=i:
                    num-=i;
                    roman+=digits[i];
                    break 
                    
        return roman

            
        
        
            
            
            
            
    
        
            