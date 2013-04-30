import os

__author__ = 'Maximilian Berger'

from urllib.error import HTTPError, URLError
from urllib.request import urlopen, HTTPBasicAuthHandler, HTTPPasswordMgrWithDefaultRealm
from SoftParser import SoftParser
from Softq_AccessData import softq_user
from Softq_AccessData import softq_password
from urllib import request

base_url = 'http://www.soft-eng.de/2013_1/softq/'
url = base_url+'semesterplan_softq.html'
res = urlopen(url)
dat = res.read().decode("iso-8859-1")
parser = SoftParser(base_url)
parser.feed(dat)
download_list = parser.getLinkList()

# Create an OpenerDirector with support for Basic HTTP Authentication...
password_mgr = HTTPPasswordMgrWithDefaultRealm()
password_mgr.add_password(None,
                          base_url,
                          softq_user,
                          softq_password)
auth_handler = HTTPBasicAuthHandler(password_mgr)
opener = request.build_opener(auth_handler)

try:
    for u in download_list:
        print("Downloading: "+u.__repr__())
        f = open(u.getName(), 'wb')
        pdf_dat = opener.open(u.getUrl())
        f.write(pdf_dat.read())
        f.close()
except (HTTPError, URLError) as e:
    print(e.__str__() + " Link: " + u.getUrl())
    f.close()
    os.remove(u.getName())

