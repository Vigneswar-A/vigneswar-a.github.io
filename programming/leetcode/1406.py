class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        
        sumtotal,multotal=0,1
        
        while n!=0:
            sumtotal,multotal,n=sumtotal+(dig:=(n%10)),multotal*dig,n//10
        
        return multotal-sumtotal
        