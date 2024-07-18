import re
pattern=re.compile(r'([\w.]+)([+\w.]*)(@[\w.]+)')
class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        mails=set()      
        for mail in emails:
            s=pattern.match(mail).groups()
            mails.add((s[0].replace('.',''),s[-1]))        
        return len(mails)
            
            
            
            
        
        
        