# -*- coding: utf-8 -*-
"""
Created on Thu Sep 23 20:20:38 2021

@author: NUGI
"""
import math

class proses:
    def jarak(self, data1, data2):
        n=len(data1)
        total=0
        for i in range (n):
            total=total+math.pow(data1[i]-data2[i],2)
        return math.sqrt(total)

obj=proses()
jarak=obj.jarak([1,2], [3,3])
print("jarak", jarak)


class kmeans(proses):
    data=[]
    nClus=[]
    centroid=[]

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

#main
data = [[1,2], [3,4], [2,3], [9,2], [8,9], [2,6], [8,1], [9,5], [8,9], [5,8], [8,8]]
nclus = 3
obj_kmeans= kmeans(data,nclus)
obj_kmeans.initCentroidStatic()
dist=obj_kmeans.getJarakSatuDataToCentroid(0)
print("jarak centroid", dist)
        