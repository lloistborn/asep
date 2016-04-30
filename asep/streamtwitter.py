import tweepy,SearchTwitter,Tweet_Normalize,Pre_Processing,Dokument_Frequency,K_Means,Database,sys,os
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from pprint import pprint
import datetime


class StreamTwitter(tweepy.StreamListener):
    def on_status(self,status):
        waktu = datetime.datetime.now()
        jam_awal=int(waktu.hour)
        menit_awal=int(waktu.minute)
        detik_awal=int(waktu.second)
        print jam_awal,menit_awal,detik_awal        
        auth = tweepy.OAuthHandler("tSKHrFs1FJEnlG83jKZ4kg", "qicqClUVx9yQVRimonmBEwgTNvneiEdS0y9NcxzhI8")
        auth.set_access_token("1885903182-At8xfHwoaCVJ1VOHbzvWCtPIvz3IYg4jKvtOK45", "yXVhHrKIhxnARYOsM6p7oYZAxfgM13cWdrhDqKY0")
        api=tweepy.API(auth)        
        temp=status.text
        temp=temp.replace('@bot_riview','')
        temp=temp.strip()
        cari=SearchTwitter.SearchTwitter()
        kicauan=cari.SearchKicauan(temp) 
        if len(kicauan)> 0:
            normalize=Tweet_Normalize.Tweet_Normalize()
            kicauan=normalize.remove_unique_character(kicauan)
            kicauan=normalize.dictionary_formalize(kicauan)
            kicauan_asli=kicauan
            
            prepro=Pre_Processing.Pre_Processing()
            kicauan=prepro.stopword_removal(kicauan)
            kicauan=prepro.tokenizer_with_dic(kicauan)
            
            DF=Dokument_Frequency.Dokument_Frequency()
            DF_Pos=DF.hitung_positif(kicauan)
            DF_Neg=DF.hitung_negatif(kicauan)
            
            kmeans=K_Means.K_Means()
            hasil=kmeans.cluster(DF_Pos,DF_Neg)
            #print len(hasil[0]),len(hasil[1]),len(hasil[2])
            pos=float(len(hasil[0])*100)/float(len(kicauan_asli))
            neg=float(len(hasil[1])*100)/float(len(kicauan_asli))
            net=float(len(hasil[2])*100)/float(len(kicauan_asli))
            #print len(hasil[0]),len(hasil[1]),len(hasil[2]),len(kicauan_asli)
            dtbs=Database.Database()
            for i in range(0,len(hasil)):
                for j in range(0,len(hasil[i])):
                    dtbs.masukan_kicauan(temp,kicauan_asli[hasil[i][j]],i+1)
            print "berhasil ditelusuri"     
            balasan=temp+" mempunyai sentimen "+str(("%.2f" % pos))+" % positif, "+ str(("%.2f" % neg))+" % negatif, dan "+ str(("%.2f" % net))+" % netral"
            for timeline in api.user_timeline():
                if balasan in timeline.text:
                    api.destroy_status(timeline.id)
            api.update_status("@"+status.user.screen_name+" "+balasan)
        else :
            balasan="@"+status.user.screen_name+" Topik tidak ditemukan silahkan masukan topik lain"
            for timeline in api.user_timeline():
                if balasan in timeline.text:
                    api.destroy_status(timeline.id)
            api.update_status(balasan)
        waktu = datetime.datetime.now()
        jam_akhir=int(waktu.hour)
        menit_akhir=int(waktu.minute)
        detik_akhir=int(waktu.second)
        print jam_akhir,menit_akhir,detik_akhir
        print "selish waktunya adaalah jam : "+str(jam_awal-jam_akhir)+" menit "+str(abs(menit_awal-menit_akhir))+" detik "+str(abs(detik_awal-detik_akhir))           
            
    def on_error(self, status_code):
        print >> sys.stderr, 'Encountered error with status code:', status_code
        return True # Don't kill the stream

    def on_timeout(self):
        print >> sys.stderr, 'Timeout...'
        return True # Don't kill the stream        



