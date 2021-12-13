# -*- coding: utf-8 -*-
"""
Created on Thu Sep 23 21:05:24 2021

@author: NUGI
"""

from kmeans3 import kmeans
            
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
            
#main
data=[[1,2], [3,4], [2,3], [9,2], [8,9], [2,6], [8,1], [9,5], [8,9], [5,8], [8,8]]
ncluster=3

#obj
obj_kmeans= kmeans(data,ncluster)
obj_kmeans.initCentroidStatic()
obj_kmeans.getAllJarak()
obj_kmeans.getAnggota()
obj_kmeans.getCentroid()

#print
print(obj_kmeans.centroid)