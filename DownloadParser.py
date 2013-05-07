from html.parser import HTMLParser
from urllib.parse import quote
from DownloadFile import DownloadFile

__author__ = 'Maximilian Berger'


class DownloadParser(HTMLParser):

    def __init__(self, base_url):
        super(DownloadParser, self).__init__()
        self.base_url = base_url
        self.linkList = list()
        self.i = 0

    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            raw_link = attrs[0][1]
            if raw_link.endswith(('.pdf', '.class', '.java', '.jar', '.zip', '.doc')):
                normalized_url = quote(self.base_url + raw_link, safe="%/:=&?~#+!$,;'@()*[]")
                name = self.i.__str__()+"-"+raw_link[6:]
                self.i += 1
                self.linkList.append(DownloadFile(normalized_url, name))

    def getLinkList(self):
        return self.linkList
