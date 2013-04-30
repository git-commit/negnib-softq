__author__ = 'Maximilian Berger'


class pdf_doc(object):
    def __init__(self, url, name):
        self.url = url
        self.name = name
    def __str__(self):
        return self.name +": "+self.url
    def __repr__(self):
        return self.name +": "+self.url
    def getUrl(self):
        return self.url
    def getName(self):
        return self.name