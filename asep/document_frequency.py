import nltk

from .kamus import Kamus

class DocumentFrequency(object):
    def __init__(self):
        self.__DF_Positif=[]
        self.__DF_Negatif=[]
        self.__kms=Kamus.Kamus()

    def hitung_positif(self,kicauan):
        pos=self.__kms.kata_positif()
        positif=nltk.word_tokenize(pos)
        for i in range(len(kicauan)):
            k=0;
            for kic in kicauan[str(i)]:
                for j in range(len(positif)):
                    if positif[j]==kic:
                        k=k+1
            self.__DF_Positif.append(k)
        return self.__DF_Positif
    
    def hitung_negatif(self,kicauan):
        neg=self.__kms.kata_negatif()
        negatif=nltk.word_tokenize(neg)
        for i in range(len(kicauan)):
            k=0;
            for kic in kicauan[str(i)]:
                for j in range(len(negatif)):
                    if negatif[j]==kic:
                        k=k+1
            self.__DF_Negatif.append(k)
        return self.__DF_Negatif
