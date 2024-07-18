class Solution:
    def reformat(self, s: str) -> str:
        nums=[]
        chars=[]
        for c in s:
            if c.isdigit():
                nums.append(c)
            else:
                chars.append(c)
        if len(nums)==len(chars):
            string=""
            for i in range(len(nums)):
                string+=nums[i]+chars[i]
            return string
        elif len(nums)==len(chars)-1:
            string=chars[0]
            for i in range(1,len(chars)):
                string+=nums[i-1]+chars[i]
            return string
        elif len(nums)==len(chars)+1:
            string=nums[0]
            for i in range(1,len(nums)):
                string+=chars[i-1]+nums[i]
            return string
        else:
            return ''
                
            
            

        
        