# """
# This is HtmlParser's API interface.
# You should not implement it, or speculate about its implementation
# """
#class HtmlParser(object):
#    def getUrls(self, url):
#        """
#        :type url: str
#        :rtype List[str]
#        """

class Solution:
    
    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:
        try:
            if startUrl in self.visited:
                return []
        except:
            self.visited = set()
        self.visited.add(startUrl)
        hostname = re.search(r"http://([aA-zZ.]+)(?:/|/b)*", startUrl).group(1)
        res  = [startUrl]
        for next_url in htmlParser.getUrls(startUrl):
            if hostname in next_url:
                res.extend(self.crawl(next_url, htmlParser))
                
        return res
            