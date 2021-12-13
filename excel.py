# -*- coding: utf-8 -*-
"""
Created on Fri Oct  1 15:21:07 2021

@author: NUGI
"""

#Import
import pandas as panda
from randomRangeValue import ClusteringKmeans

#Inisialisasi
df = panda.read_excel('Book1.xlsx')
df = panda.DataFrame(df, columns=(['x', 'y']))
data = df.values.tolist()
nCluster = 3

#Pembuat Obj
objek = ClusteringKmeans(data, nCluster)
objek.learning()
objek.plottingError()
objek.scatterDataCentroid()

#Cetak
print("Centroid = ", objek.centroid)
print("\n Index anggota data = ", objek.index)
print("\n Sum of Distance Semua Iterasi = ", objek.error)
print("\n Sum Of Distance Akhir =", objek.error[len(objek.error)-1])