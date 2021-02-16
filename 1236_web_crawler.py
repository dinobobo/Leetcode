# """
# This is HtmlParser's API interface.
# You should not implement it, or speculate about its implementation
# """
# class HtmlParser(object):
#    def getUrls(self, url):
#        """
#        :type url: str
#        :rtype List[str]
#        """

class Solution:
    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:
        def find_host(url):
            slash_num = 0
            for i in range(len(url)):
                if url[i] == '/':
                    slash_num += 1
                if slash_num == 3:
                    break
            return url if slash_num != 3 else url[:i]

        def dfs(url):
            ans = []
            if find_host(url) != host or url in visited:
                return []
            ans.append(url)
            visited.add(url)
            for u in get_url(url):
                ans += dfs(u)
            return ans

        visited = set()
        get_url = htmlParser.getUrls
        host = find_host(startUrl)
        return dfs(startUrl)
