# -*- coding: utf-8 -*-
"""
Created on Thu Sep 23 20:47:57 2021

@author: NUGI
"""

import math

class proses:
    def jarak(self, data1, data2):
        n=len(data1)
        total=0
        for i in range (0,n):
            total=total+math.pow(data1[i]-data2[i],2)
        return math.sqrt(total)
    
    def getIndexMin(self,data):
        n=len(data)
        index=0
        min=data[0]
        for i in range (1,n):
            if min>data[i]:
                index=i
                min=data[i]
        return index

class kmeans(proses):
    data=[]
    nClus=[]
    centroid=[]
    jarak=[]
    index=[]
    
    def __init__(self,data,ncluster):
        kmeans.data=data
        kmeans.nCluster=ncluster
    
    def initCentroidStatic(self):
        arr=[[3,3], [0,1], [8,1]]
        kmeans.centroid=arr
    
    def getJarakSatuDataToCentroid(self,index):
        n=kmeans.nCluster
        jarak=0
        dist=[]
        for i in range (n):
            jarak=proses.jarak(self,kmeans.data[index],kmeans.centroid[i])
            dist.append(jarak)
        return dist
    
    def getAllJarak(self):
        n=len(kmeans.data)
        dist=[]
        for i in range (n):
            dist.append(self.getJarakSatuDataToCentroid(i))
            kmeans.jarak=dist
            
    def getAnggota(self):
        n=len(kmeans.data)
        x=kmeans.jarak
        ind=[]
        for i in range (n):
            ind.append(proses.getIndexMin(self, x[i]))
            kmeans.index=ind

#main
data = [[1,2], [3,4], [2,3], [9,2], [8,9], [2,6], [8,1], [9,5], [8,9], [5,8], [8,8]]
nclus = 3

#obj
obj_kmeans= kmeans(data,nclus)
obj_kmeans.initCentroidStatic()
obj_kmeans.getAllJarak()
obj_kmeans.getAnggota()
print("index anggota", obj_kmeans.index)