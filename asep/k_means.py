import math

class K_Means(object):
    def __init__(self): 
        self.__centeroid_x=[1,0,0]
        self.__centeroid_y=[0,1,0]
        self.__check=False
        self.__cluster=[[] for x in xrange (4)]
        self.__cluster_temp=[[] for x in xrange (4)]        
        
    def cluster(self,DF_x,DF_y): 
        self.__cluster_awal(DF_x,DF_y)
        while self.__check != True:
            self.__cluster_temp=self.__cluster
            self.__cluster=[[] for x in xrange (4)]
            for j in range(len(self.__centeroid_x)):
                temp=0 
                for k in range(len(self.__cluster_temp[j])-1):
                    temp=temp+DF_x[self.__cluster_temp[j][k]]
                if self.__cluster_temp[j]:
                    self.__centeroid_x[j]=int(temp/len(self.__cluster_temp[j]))
                else:
                    self.__centeroid_x[j]=self.__centeroid_x[j]
            for j in range(len(self.__centeroid_y)):
                temp=0 
                for k in range(len(self.__cluster_temp[j])-1):
                    temp=temp+DF_y[self.__cluster_temp[j][k]]
                if self.__cluster_temp[j]:
                    self.__centeroid_y[j]=int(temp/len(self.__cluster_temp[j]))
                else:
                    self.__centeroid_y[j]=self.__centeroid_y[j]
            self.__cluster_awal(DF_x,DF_y)               
            if self.__cluster==self.__cluster_temp:
                self.__check=True
        return self.__cluster_temp
    
    def __cluster_awal(self,DF_x,DF_y):
        for i in range(0,len(DF_x)):
                    temp_c1=math.sqrt((math.pow((DF_x[i]-self.__centeroid_x[0]),2))+(math.pow((DF_y[i]-self.__centeroid_y[0]),2)))
                    temp_c2=math.sqrt((math.pow((DF_x[i]-self.__centeroid_x[1]),2))+(math.pow((DF_y[i]-self.__centeroid_y[1]),2)))
                    temp_c3=math.sqrt((math.pow((DF_x[i]-self.__centeroid_x[2]),2))+(math.pow((DF_y[i]-self.__centeroid_y[2]),2)))
                    if   (temp_c1<temp_c2 and temp_c1<temp_c3):
                        self.__cluster[0].append(i)
                    elif (temp_c2<temp_c1 and temp_c2<temp_c3):
                        self.__cluster[1].append(i)
                    elif ((temp_c3<temp_c1 and temp_c3 <temp_c2) or temp_c1==temp_c2 or (DF_x[i]==DF_y[i])):                     
                        self.__cluster[2].append(i)
                    else :                      
                        self.__cluster[3].append(i)
                           

        
                            
                           
                       
