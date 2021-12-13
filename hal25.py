# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
class kmeans():
    data=[]
    nClus=[]
    
    def __init__(self, data,nClus):
        kmeans.data = data
        kmeans.nClus = nclus
        centroid=[]
        
    def initCentroidStatic(self):
        arr=[[3,3], [0,1], [8,1]]
        kmeans.centroid=arr

#main
data = [[1,2], [3,4], [2,3], [9,2], [8,9], [2,6], [8,1], [9,5], [8,9], [5,8], [8,8]]
nclus = 3

obj_kmeans= kmeans(data,nclus)
obj_kmeans.initCentroidStatic()
print("Data", obj_kmeans.data)
print("nclus", obj_kmeans.nClus)
print("centroid", obj_kmeans.centroid)