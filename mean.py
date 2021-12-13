# -*- coding: utf-8 -*-
"""
Created on Thu Sep 23 21:05:24 2021

@author: NUGI
"""

from kmeans2 import kmeans
import matplotlib.pyplot as plt
import numpy as np
            
class ClusteringKmeans(kmeans):
    error=[]
    
    def __init__(self,data,ncluster):
        kmeans.data=data
        kmeans.nCluster=ncluster
        kmeans.initCentroidStatic(self)
    
    def learning(self):
        errorLama=-1
        errorBaru=0
        
        while errorLama != errorBaru:
            errorLama=errorBaru
            kmeans.getAllJarak(self)
            kmeans.getAnggota(self)
            kmeans.getSumOfDistance(self)
            kmeans.getCentroid(self)
            errorBaru=kmeans.error
            ClusteringKmeans.error.append(errorBaru)
        
    # def plottingError(self):
    #     plt.plot(self.error)
    #     plt.show()
    
    # def scatterDataCentroid(self):
    #     x=self.kumpulAnggotaPercluster()
    #     for i in range (len(x)):
    #         temp=np.array(x[i])
    #         plt.scatter(temp[:,0], temp[:,1])
    #         cent=np.array(kmeans.centroid)
    #         plt.scatter(cent[:,0], cent[:,1], marker='x')
    #         plt.show()
        
    # def kumpulAnggotaPercluster(self):
    #     n=len(kmeans.data)
    #     m=kmeans.nCluster
    #     Datacluster=[]
    #     for i in range (m):
    #         temp=[]
    #         for j in range (n):
    #             if (i==kmeans.index[j]):
    #                 temp.append(kmeans.data[j])
    #                 Datacluster.append(temp)
    #                 return Datacluster
            
#main
data=[[1,2], [3,4], [2,3], [9,2], [8,9], [2,6], [8,1], [9,5], [8,9], [5,8], [8,8]]
ncluster=3

#obj
# objek=ClusteringKmeans(data, ncluster)
# objek.learning()
# objek.plottingError()
# objek.scatterDataCentroid()
obj_kmeans= kmeans(data,ncluster)
obj_kmeans.initCentroidStatic()
obj_kmeans.getAllJarak()
obj_kmeans.getAnggota()
obj_kmeans.getSumOfDistance()
obj_kmeans.getCentroid()


#print
# print("centroid", objek.centroid)
# print("index anggota data", objek.index)
# print("sum distance semua iterasi", objek.error)
# print("sum distance akhir", objek.error[len(objek.error)-1])
print(obj_kmeans.centroid)