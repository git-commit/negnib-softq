from html.parser import HTMLParser
from urllib.parse import quote
from Pdf_Document import pdf_doc

__author__ = 'Maximilian Berger'


class SoftParser(HTMLParser):

    def __init__(self, base_url):
        super(SoftParser, self).__init__()
        self.base_url = base_url
        self.linkList = list()

    def handle_starttag(self, tag, attrs):
        if (tag == 'a'):
          raw_link = attrs[0][1]
          if('pdf' in raw_link):
            normalized_url = quote(self.base_url + raw_link,safe="%/:=&?~#+!$,;'@()*[]")
            name = raw_link[6:]
            self.linkList.append(pdf_doc(normalized_url,name))
    def getLinkList(self):
        return self.linkList
