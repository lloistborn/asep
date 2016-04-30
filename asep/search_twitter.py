import tweepy, time

class SearchTwitter(object):
    
    def __init__(self):
        auth = tweepy.OAuthHandler("iJx3wTVeN0Kq9kw5Az3Dg", "ew0UH2mE7v3X8fXVNrviURsTG2KOtDR7wfOilgj2w")
        auth.set_access_token("89917052-4VPBIVRGLzPT7VNFXWm9mLX7Kq3IGsYDjLpRBXt7r", "Os1AGJ79g4MOhJLWJqvmDflhoZiUrlbP07TsPzkiBFc")
        self.__myapi = tweepy.API(auth)
        self.__kicauan=[]
        
    def SearchKicauan(self,masukan):
        start=time.clock()
        for status in tweepy.Cursor(self.__myapi.search,masukan,lang="id",result_type="recent").items(100):
            self.__kicauan.append(status.text)
        return self.__kicauan
    


    

