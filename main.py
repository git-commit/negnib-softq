import os

__author__ = 'Maximilian Berger'

from urllib.error import HTTPError, URLError
from urllib.request import urlopen, HTTPBasicAuthHandler, HTTPPasswordMgrWithDefaultRealm
from DownloadParser import DownloadParser
from AccessData import softq_user
from AccessData import softq_pw
from urllib import request
from hashlib import md5

base_url = 'http://www.soft-eng.de/2013_1/softq/'
url = base_url+'semesterplan_softq.html'
res = urlopen(url)
dat = res.read().decode("iso-8859-1")
parser = DownloadParser(base_url)
parser.feed(dat)
download_list = parser.getLinkList()

# Create an OpenerDirector with support for Basic HTTP Authentication...
password_mgr = HTTPPasswordMgrWithDefaultRealm()
password_mgr.add_password(None,
                          base_url,
                          softq_user,
                          softq_pw)
auth_handler = HTTPBasicAuthHandler(password_mgr)
opener = request.build_opener(auth_handler)

if not os.path.exists('files'):
    os.mkdir('files')

os.chdir('files')

try:
    for u in download_list:
        print("Downloading: "+u.__repr__())
        pdf_dat = opener.open(u.getUrl())
        with open(u.getName(), 'wb') as f:
            f.write(pdf_dat.read())

except (HTTPError, URLError) as e:
    print(e.__str__() + " Link: " + u.getUrl())
    os.remove(u.getName())

