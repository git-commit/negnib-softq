from AccessData import softq_user, softq_pw, mmi_user, mmi_pw, softq_url, mmi_url, j3d_url, j3d_user, j3d_pw
from SimpleDownloader import SimpleDownloader


if __name__ == '__main__':
    soft = SimpleDownloader(softq_url, softq_user, softq_pw, 'iso-8859-1')
    soft.start()
    soft.join()

    #mmi = SimpleDownloader(mmi_url, mmi_user, mmi_pw)
    #j3d = SimpleDownloader(j3d_url, j3d_user, j3d_pw)

__author__ = 'Maximilian Berger'
