# _*_ coding:utf-8 _*_
import json
import re
import urllib
import time

class Tools(object):

    def timeStampToDate(self, timestamp):
        timeArray = time.localtime(int(timestamp))
        otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
        return otherStyleTime

    def insert(self, original, new, pos):
        return original[:pos] + new + original[pos:]

    def json_format_data(self, _str, url):
        pattern = re.compile(r'(\w{8})wangning')
        json_name = pattern.search(url).group()
        json_str = _str[9:(len(_str)-1)]
        _json = json.loads(json_str)
        datas = _json[json_name]
        return datas

    def isUrl(self, url):
        pattern = re.compile(r'(http|ftp|https):\/\/[\w\-_]+(\.[\w\-_]+)+([\w\-\.,@?^=%&amp;:/~\+#]*[\w\-\@?^=%&amp;/~\+#])?')
        match = pattern.match(url)
        if match:
            return True
        else:
            return False

    def get_url_date(self, url , start , size):
        str_uri = str(start) + '-' + str(size) + '.html'
        new_url = urllib.parse.urljoin(url , str_uri)
        return new_url

    def already_crawler_url(self , url , path='../CrawlerData/'):
        file = open(path + 'url.txt', 'r')
        if url in file.read():
            return True
        else:
            return False


    def write_url_to_file(self , url, path='../CrawlerData/'):
        filename=path + 'url.txt'
        file=open(filename, 'a')

        file.write(str(url))
        file.close()

if __name__ == "__main__":
    tools = Tools();
    match = tools.timeStampToDate("1491328679")
    print(match)
