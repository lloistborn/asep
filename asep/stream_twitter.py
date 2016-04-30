from .document_frequency import DocumentFrequency
from .k_means import KMeans 
from .pre_processing import PreProcessing 
from .search_twitter import SearchTwitter  
from .tweet_normalize import TweetNormalize 

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from pprint import pprint
import tweepy
import datetime
import sys, os

class StreamTwitter():

    def stream(self,status):
        # print(status.text)
        # waktu   = datetime.datetime.now()
        # jam_awal=int(waktu.hour)
        # menit_awal=int(waktu.minute)
        # detik_awal=int(waktu.second)
        # print(jam_awal,menit_awal,detik_awal)        
        # auth = OAuthHandler("tSKHrFs1FJEnlG83jKZ4kg", "qicqClUVx9yQVRimonmBEwgTNvneiEdS0y9NcxzhI8")
        # auth.set_access_token("1885903182-At8xfHwoaCVJ1VOHbzvWCtPIvz3IYg4jKvtOK45", "yXVhHrKIhxnARYOsM6p7oYZAxfgM13cWdrhDqKY0")
        # api=tweepy.API(auth)        
        # temp=status.text
        # temp=temp.replace('@bot_riview','')
        # temp=temp.strip()
        cari=SearchTwitter()
        
        kicauan=cari.SearchKicauan(status) 
        tempKicauan = kicauan
        if len(kicauan)> 0:
            normalize=TweetNormalize()
            kicauan=normalize.remove_unique_character(kicauan)
            kicauan=normalize.dictionary_formalize(kicauan)
            kicauan_asli=kicauan
            print('kicauan')
            
            prepro  = PreProcessing()
            kicauan = prepro.stopword_removal(kicauan)
            kicauan = prepro.tokenizer_with_dic(kicauan)
            print('preprop')
            

            DF      = DocumentFrequency()
            DF_Pos  = DF.hitung_positif(kicauan)
            DF_Neg  = DF.hitung_negatif(kicauan)
            print('df')
            

            kmeans  = KMeans()
            hasil   = kmeans.cluster(DF_Pos,DF_Neg)
            #print len(hasil[0]),len(hasil[1]),len(hasil[2])
            pos=float(len(hasil[0])*100)/float(len(kicauan_asli))
            neg=float(len(hasil[1])*100)/float(len(kicauan_asli))
            net=float(len(hasil[2])*100)/float(len(kicauan_asli))
            #print len(hasil[0]),len(hasil[1]),len(hasil[2]),len(kicauan_asli)
            # dtbs=Database.Database()
            # for i in range(0,len(hasil)):
            #     for j in range(0,len(hasil[i])):
            #         dtbs.masukan_kicauan(temp,kicauan_asli[hasil[i][j]],i+1)
            # print("berhasil ditelusuri")     
            balasan=temp+" mempunyai sentimen "+str(("%.2f" % pos))+" % positif, "+ str(("%.2f" % neg))+" % negatif, dan "+ str(("%.2f" % net))+" % netral"
            # for timeline in api.user_timeline():
                # if balasan in timeline.text:
                    # api.destroy_status(timeline.id)
            # api.update_status("@"+status.user.screen_name+" "+balasan)
            print('kmeans')

        else :
            balasan="@"+status.user.screen_name+" Topik tidak ditemukan silahkan masukan topik lain"
            # for timeline in api.user_timeline():
            #     if balasan in timeline.text:
            #         api.destroy_status(timeline.id)
            # api.update_status(balasan)
        # waktu = datetime.datetime.now()
        # jam_akhir=int(waktu.hour)
        # menit_akhir=int(waktu.minute)
        # detik_akhir=int(waktu.second)
        
        # print(balasan)
        # print(jam_akhir,menit_akhir,detik_akhir)
        # print("selish waktunya adaalah jam : "+str(jam_awal-jam_akhir)+" menit "+str(abs(menit_awal-menit_akhir))+" detik "+str(abs(detik_awal-detik_akhir)))           
        
        return tempKicauan, balasan, pos, neg, net

    # def on_error(self, status_code):
    #     print >> sys.stderr, 'Encountered error with status code:', status_code
    #     return True # Don't kill the stream

    # def on_timeout(self):
    #     print >> sys.stderr, 'Timeout...'
    #     return True # Don't kill the stream        



