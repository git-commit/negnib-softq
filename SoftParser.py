from html.parser import HTMLParser
from Pdf_Document import pdf_doc

__author__ = 'Maxi'


class SoftParser(HTMLParser):
    linkList = list()

    def __init__(self, base_url):
        super(SoftParser, self).__init__()
        self.base_url = base_url

    def handle_starttag(self, tag, attrs):
        if (tag == 'a') and ('pdf' in attrs[0][1]):
            self.linkList.append(pdf_doc(self.base_url + attrs[0][1],attrs[0][1][6:]))
    def getLinkList(self):
        return self.linkList