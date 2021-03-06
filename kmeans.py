# -*- coding: utf-8 -*-
"""
Created on Thu Sep 23 20:35:03 2021

@author: DIMAS
"""
import math
import random as rand
class proses:
    def jarak(self,data1,data2):
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
    
    def mean(self,data):
        n=len(data)
        m=len(data[0])
        tot=[0]*m
        for i in range(n):
            for j in range (m):
                tot[j]=tot[j]+data[i][j]
        for i in range(m):
            tot[i]=tot[i]/n
        return tot

class kmeans(proses):
    data=[]
    nCluster=0
    centroid=[]
    jarak=[]
    index=[]
    error=0
    
    def __init__(self,data,ncluster):
        kmeans.data=data
        kmeans.nCluster=ncluster
        
    def initCentroid(self):
        cent=[]
        for i in range (self.nCluster):
            x=[]
            for j in range(len(self.data[0])):
                [min,max]=proses.getMinMax(self, self.data, j)
                x.append(rand.randint(min,max))
            cent.append(x)
        kmeans.centroid=cent;
        
    def initCentroidStatic(self):
        arr=[[3,3],[0,1],[8,1]]
        kmeans.centroid=arr
        
    def getJarakSatuDataToCentroids(self,index):
        n=kmeans.nCluster
        jarak=0
        dist=[]
        
        for i in range(n):
            jarak=proses.jarak(self,kmeans.data[index],
                               kmeans.centroid[i])
            dist.append(jarak)
        return dist
    
    def getAllJarak(self):
        n=len(kmeans.data)
        dist=[]
        for i in range(n):
            dist.append(self.getJarakSatuDataToCentroids(i))
            kmeans.jarak=dist
            
    def getAnggota(self):
        n=len(kmeans.data)
        x=kmeans.jarak
        ind=[]
        
        for i in range(n):
            ind.append(proses.getIndexMin(self,x[i]))
            kmeans.index=ind
            
    def getSumOfDistance(self):
        n=len(self.jarak)
        error=0
        
        for i in range (n):
            error=error+self.jarak[i][self.index[i]]
        kmeans.error=error
            
    def getCentroid(self):
        n=len(kmeans.jarak)
        for i in range (self.nCluster):
            ang=[]
            for j in range (n):
                if self.index[j]==i:
                    ang.append(kmeans.data[j])
                if ang!=[]:
                    kmeans.centroid[i]=proses.mean(self,ang)
                else:
                    kmeans.centroid[i]=ang
    
# #Main Program
# data=[[1,2],[3,4],[2,3],[9,2],[8,9],[2,6],[8,1],[9,5],[8,9],[5,8],[8,8]]
# ncluster=3

# #Pembuatan Objek dan Testing 
# obj_kmeans=kmeans(data,ncluster)
# obj_kmeans.initCentroidStatic()
# obj_kmeans.getAllJarak()
# obj_kmeans.getAnggota()
# #obj_kmeans.getSumOfDistance()
# obj_kmeans.getCentroid()
# print("Centroid Baru :", obj_kmeans.centroid)