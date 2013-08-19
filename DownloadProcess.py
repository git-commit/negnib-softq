from multiprocessing import Process
from time import sleep
import urllib.request

__author__ = 'Maxi'

class DownloadProcess(Process):
    def __init__(self, url, username, password, downloadSemaphore):
        super(DownloadProcess, self).__init__()
        self.url = url
        self.username = username
        self.password = password
        self.downloadSemaphore = downloadSemaphore

    def download(self):
                # Create an OpenerDirector with support for Basic HTTP Authentication...
                auth_handler = urllib.request.HTTPBasicAuthHandler()
                auth_handler.add_password('softq',self.url,self.username,self.password)
                opener = urllib.request.build_opener(auth_handler)
                dat = opener.open(self.url)
                #Find file name of file
                filename = self.url.rpartition('/')[2]
                file = open('soft/'+filename, 'wb')
                file.write(dat.read())
                file.close()
       
    def run(self):
        self.downloadSemaphore.acquire()
        self.download()
        self.downloadSemaphore.release()