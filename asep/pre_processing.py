import nltk 
from .document_frequency, kamus import DocumentFrequency, Kamus

class PreProcessing(object):
    def __init__(self):
        self.__kms=Kamus.Kamus()
        
    def stopword_removal(self,kicauan):
        stopword=self.__kms.kata_stopword()
        for i in range(0,len(kicauan)):
            cacah_kicauan=nltk.word_tokenize(kicauan[i])
            for j in range(0,len(cacah_kicauan)):
                if cacah_kicauan[j] in stopword:
                    cacah_kicauan[j]=""
            kicauan[i]=' '.join(cacah_kicauan)
        return kicauan

    def tokenizer_with_dic(self,kicauan):
        dic_kicauan={}
        for i in range(0,len(kicauan)):
            cacah_kicauan=nltk.word_tokenize(kicauan[i])
            dic_kicauan[str(i)]=cacah_kicauan 
        return dic_kicauan





        
