from multiprocessing import Semaphore
from multiprocessing.process import Process
from urllib.parse import urljoin, quote
from urllib.request import urlopen
from bs4 import BeautifulSoup
from DownloadProcess import DownloadProcess


__author__ = 'Maxi'

accepted_files = ('.pdf', '.class', '.java', '.jar', '.zip', '.doc')

def validDocument(link):
    href = link.get('href')
    return (href is not None) and href.endswith(accepted_files)

class SimpleDownloader(Process):
    def __init__(self, url, username, password, encoding = 'utf-8'):
        super(SimpleDownloader,self).__init__()
        self.url = url
        self.username = username
        self.password = password
        self.encoding = encoding
        self.downloadSemaphore = Semaphore(4)

    def run(self):
        raw_request = urlopen(self.url)
        dat = raw_request.read().decode(self.encoding)
        soup = BeautifulSoup(dat)
        for link in soup.find_all('a'):
            if validDocument(link):
                DownloadProcess(self.generateUrl(link), self.username, self.password, self.downloadSemaphore).start()


    def generateUrl(self,link):
        return str(quote(urljoin(self.url, link.get('href')), safe="%/:=&?~#+!$,;'@()*[]"))

    def getLinks(self):
        return None
