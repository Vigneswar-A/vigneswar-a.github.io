ipv4 = re.compile(r'^((25[0-5]|(2[0-4]|1\d|[1-9]|)\d)\.?\b){4}$')
ipv6 = re.compile(r'^([0-9a-fA-F]{0,4}:?\b){8}$')

class Solution:
    def validIPAddress(self, queryIP: str) -> str:
          
        if ipv4.fullmatch(queryIP):
            return 'IPv4'
        elif ipv6.fullmatch(queryIP):
            return 'IPv6'
        else:
            return 'Neither'
        
        