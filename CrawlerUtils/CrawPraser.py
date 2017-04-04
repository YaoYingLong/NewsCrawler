from bs4 import BeautifulSoup


class JsonParser(object):

    def getNewContent(self , html_cont):
        _soup = BeautifulSoup(html_cont , 'html.parser')
        try:
            html_content = self.removeTag(_soup, ['a' , 'img'])
            contents = html_content.find('div', class_='content').find_all('p')
            news_content = ''.join(map(lambda content : ''.join(content.get_text().split()) , contents))
        except Exception as e:
            print("Exception: 获取新闻正文出现异常")
            return None
        return news_content

    def removeTag(self , soup, tagNameList):
        for tagName in tagNameList:
            [tag.extract() for tag in soup.find_all(tagName)]
        soup.prettify()
        return soup


