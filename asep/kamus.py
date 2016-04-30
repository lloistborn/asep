import os
from django.conf import settings

class Kamus(object):
    def __init__(self):
        self.__file_stopword    = os.path.join(settings.MEDIA_ROOT, "stopword.txt")
        self.__kbba_file        = os.path.join(settings.MEDIA_ROOT, "kbba.txt")
        self.__file_positif     = os.path.join(settings.MEDIA_ROOT, "positif.txt")
        self.__file_negatif     = os.path.join(settings.MEDIA_ROOT, "negatif.txt") 

    def kata_stopword(self):
        f           = open(self.__file_stopword,"r")
        stopword    = f.read().lower()  
        f.close()
        return stopword

    def kata_normalize(self):
        f           = open(self.__kbba_file,"r")
        return f

    def kata_positif(self):
        f           = open(self.__file_positif,"r")
        pos         = f.read().lower() 
        f.close()
        return pos

    def kata_negatif(self):
        f           = open(self.__file_negatif,"r")
        neg         = f.read().lower()  
        f.close()
        return neg        