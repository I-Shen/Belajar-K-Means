# -*- coding: utf-8 -*-
"""
Created on Fri Sep 24 14:05:05 2021

@author: DIMAS
"""

from kmeans import kmeans

class ClusteringKmeans(kmeans):
    error=[]
    
    def __init__(self,data,ncluster):
        kmeans.data=data
        kmeans.nCluster=ncluster
        kmeans.initCentroidStatic(self)
    def learning(self):
        errorLama=-1
        errorBaru=0
        
        while errorLama!=errorBaru:
            errorLama=errorBaru
            kmeans.getAllJarak(self)
            kmeans.getAnggota(self)
            kmeans.getSumOfDistance(self) 
            kmeans.getCentroid(self)
        errorBaru=kmeans.error
        ClusteringKmeans.error.append(errorBaru)
        
#Main Program
data=[[1,2],[3,4],[2,3],[9,2],[8,9],[2,6],[8,1],[9,5],[8,9],[5,8],[8,8]]
ncluster=3

#Pembuatan Objek dan pemanggilan method learning 
objek=ClusteringKmeans(data,ncluster)
objek.learning()

#Cetak Hasil Utama
print("centroid =",objek.centroid)
print("\n index anggota data = ", objek.index)
print("\n Sum of Distance Semua Iterasi = ",objek.error)
print("\n Sum Of Distance Akhir =", objek.error[len(objek.error)-1])