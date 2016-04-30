import re, nltk

from .kamus import Kamus

class TweetNormalize(object):
    def __init__(self):
        self.__kms=Kamus()
        
    def remove_unique_character(self,kicauan):
        for i in range(0,len(kicauan)):
            kicauan[i]=re.sub(r'(http://)*(https://)*\w+\.\w+\/\w+','',kicauan[i],flags=re.IGNORECASE)
            kicauan[i]=re.sub(r'(RT )*@\w+(:)*','',kicauan[i],flags=re.IGNORECASE)
            kicauan[i]=re.sub(r'"+|\'+|-|\\|/','',kicauan[i],flags=re.IGNORECASE)
        return kicauan
    
    def dictionary_formalize(self,kicauan):
        f=self.__kms.kata_normalize()
        for sentence in f:
            array=sentence.strip().split("\t")
            informal=array[0]
            formal=array[1]
            for i in range(0,len(kicauan)):
                cacah_kicauan=nltk.word_tokenize(kicauan[i])
                for j in range(0,len(cacah_kicauan)):
                    if cacah_kicauan[j]==informal:
                        cacah_kicauan[j]=formal
                kicauan[i]=' '.join(cacah_kicauan)
        f.close()
        return kicauan

                
        
